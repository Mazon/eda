import random
import math
import statistics
from dataclasses import dataclass, field
from typing import List, Tuple, Dict, Optional, Set

# --- Data Structures ---

@dataclass
class Stats:
    STR: int = 60
    AGI: int = 60
    LOG: int = 60
    INS: int = 60
    CHA: int = 60
    CON: int = 60

@dataclass
class Weapon:
    name: str
    damage: int
    is_ranged: bool = False
    hands: int = 1
    is_shield: bool = False
    defense: int = 0 

@dataclass
class Armor:
    name: str
    defense: int = 0

@dataclass
class Character:
    name: str
    role: str
    stats: Stats
    hp: int = 0
    max_hp: int = 0
    ip: int = 0
    max_ip: int = 0
    reactions: int = 0
    max_reactions: int = 0
    nature: str = "The Wolf"
    heritage: str = "Clansman"
    
    weapon: Weapon = field(default_factory=lambda: Weapon("Fists", 2))
    offhand: Optional[Weapon] = None
    armor: Armor = field(default_factory=lambda: Armor("Clothes", 0))
    
    skill_combat: int = 50
    skill_survival: int = 50
    skill_social: int = 50
    skill_magic: int = 50
    
    ap: int = 0
    talents: List[str] = field(default_factory=list)
    relics: List[str] = field(default_factory=list)
    marked_skills: Set[str] = field(default_factory=set)
    is_dead: bool = False
    
    # Tactical Combat States
    combat_ap: int = 0
    momentum: Optional[str] = None 
    active_defense_bonus: int = 0
    focus_points: int = 0
    is_marked: bool = False
    has_disadvantage: bool = False
    has_acted: bool = False
    took_damage_this_round: bool = False
    target_hit_this_round: Set[str] = field(default_factory=set)
    cover_type: str = "None" # "None", "Half", "Full"
    is_hunkered: bool = False
    is_suppressed: bool = False
    moved_this_turn: int = 0
    has_evasive_bonus: bool = False
    has_free_reaction: bool = False # Rule 1: First reaction after move is free
    is_charging: bool = False
    cannot_dodge: bool = False
    
    # Active Talent Buffs for current turn
    next_attack_bonus_dmg: int = 0
    next_attack_advantage: bool = False
    next_attack_overdrive: bool = False
    used_slayers_fury: bool = False
    
    def __post_init__(self):
        self.recalc_derived()
        self.full_heal()

    def recalc_derived(self):
        hp_bonus = 5 if "Endurance Training" in self.talents else 0
        self.max_hp = self.stats.CON + hp_bonus
        self.max_ip = self.stats.INS // 2
        
        natural_defense = 0
        self.natural_defense = natural_defense

        # Reactions Pool: Tens digit of AGI
        self.max_reactions = self.stats.AGI // 10
        if "Duelist" in self.talents: self.max_reactions += 1
        
        if self.reactions > self.max_reactions: self.reactions = self.max_reactions

    def full_heal(self):
        if not self.is_dead:
            self.hp = self.max_hp
            self.ip = self.max_ip
            self.reactions = self.max_reactions

    def roll_skill(self, skill_val: int, skill_name: Optional[str] = None, modifier: int = 0, advantage: bool = False, disadvantage: bool = False) -> Tuple[bool, int, int, bool]:
        target = skill_val + modifier
        
        def do_roll():
            roll = random.randint(1, 100)
            success = roll <= target
            dos = roll // 10
            if roll == 100: success = False; dos = 10 # 100 is 10 dos but always fails
            return success, roll, dos

        if (advantage and not disadvantage) or (disadvantage and not advantage):
            d1 = random.randint(0, 9)
            d2 = random.randint(0, 9)
            v1 = d1 * 10 + d2
            if v1 == 0: v1 = 100
            v2 = d2 * 10 + d1
            if v2 == 0: v2 = 100
            
            s1 = v1 <= target
            s2 = v2 <= target
            dos1 = v1 // 10 if v1 < 100 else 10
            dos2 = v2 // 10 if v2 < 100 else 10
            
            if advantage:
                if s1 and s2: res = (s1, v1, dos1) if dos1 >= dos2 else (s2, v2, dos2)
                elif s1: res = (s1, v1, dos1)
                elif s2: res = (s2, v2, dos2)
                else: res = (s1, v1, dos1) if v1 <= v2 else (s2, v2, dos2)
            else:
                if s1 and s2: res = (s1, v1, dos1) if dos1 <= dos2 else (s2, v2, dos2)
                elif s1 and not s2: res = (s2, v2, dos2)
                elif s2 and not s1: res = (s1, v1, dos1)
                else: res = (s1, v1, dos1) if v1 >= v2 else (s2, v2, dos2)
            s1, r1, d1 = res
        else:
            s1, r1, d1 = do_roll()
            
        is_crit = s1 and r1 > 0 and r1 % 11 == 0
        return s1, r1, d1, is_crit

    def take_damage(self, amount: int):
        defense = self.armor.defense + getattr(self, "natural_defense", 0)
        if "Holy Aura" in self.talents: defense += 1
        if "Defensive Stance" in self.talents: defense += 2
        if "Steel Resolve" in self.talents: defense += 2
        if self.has_evasive_bonus: defense += 3 # New Rule: +3 Defense from movement
        
        final_dmg = max(0, amount - defense)
        if final_dmg > 0:
            self.took_damage_this_round = True
            if "Iron Will" in self.talents:
                self.focus_points = min(5, self.focus_points + 1)
        self.hp -= final_dmg
        if self.hp <= 0:
            if "Unyielding Spirit" in self.talents and not getattr(self, "used_unyielding", False):
                self.hp = 1
                self.used_unyielding = True
                self.hp += 10
            else:
                self.hp = 0
                self.is_dead = True

    def gain_ap(self, amount=10):
        self.ap += amount
        self.spend_ap()

    def spend_ap(self):
        while self.ap >= 5:
            added = False
            t1_options = ["Focus", "Overdrive", "Dodge", "Parry", "Blocker", "First Strike", "The Charge"]
            for t in t1_options:
                if t not in self.talents and self.ap >= 5:
                    self.talents.append(t); self.ap -= 5; self.recalc_derived(); added = True; break
            if added: continue
            
            t2_options = ["Cleave", "Holy Aura", "Exploit Opening", "Harrying Strike", "Bloodied Fury", "Pack Tactics", "Move and Attack"]
            for t in t2_options:
                if t not in self.talents and self.ap >= 10:
                    t1_count = len([x for x in self.talents if x in t1_options])
                    t2_count = len([x for x in self.talents if x in t2_options])
                    if t1_count > t2_count:
                        self.talents.append(t); self.ap -= 10; self.recalc_derived(); added = True; break
            if not added: self.ap = 0

@dataclass
class EncounterResult:
    won: bool
    rounds: int
    party_hp_pct: float
    enemies_killed: int
    total_enemies: int
    vanguard_percentage: float = 0.0

class CombatEncounter:
    def __init__(self, name: str, enemies: List[Character], is_boss=False):
        self.name, self.enemies, self.is_boss = name, enemies, is_boss
        
    def run(self, party: List[Character], strategy: Optional[str] = None) -> EncounterResult:
        rounds = 0
        total_enemies = len(self.enemies)
        vanguard_instances = 0
        total_instances = 0
        
        while any(p.hp > 0 for p in party) and any(e.hp > 0 for e in self.enemies):
            rounds += 1
            if rounds > 50: break
            
            for c in party + self.enemies:
                c.combat_ap = 2
                c.next_attack_bonus_dmg = 0
                c.next_attack_advantage = False
                c.next_attack_overdrive = False
                c.moved_this_turn = 0
                c.attacks_this_turn = 0
                c.has_evasive_bonus = False
                c.has_free_reaction = False
                if "Vanguard Reflexes" in c.talents:
                    c.reactions = min(c.max_reactions, c.reactions + 1)
                c.momentum = None
                c.has_acted = False
                c.took_damage_this_round = False

            vanguard_players = []
            rearguard_players = []
            for p in party:
                if p.hp <= 0: continue
                total_instances += 1
                mod = 0
                if "Tempo" in p.talents: mod += 10
                success, roll, dos, crit = p.roll_skill(p.stats.AGI, modifier=mod)
                if success: 
                    vanguard_players.append(p)
                    vanguard_instances += 1
                else: 
                    rearguard_players.append(p)
            
            random.shuffle(vanguard_players)
            for p in vanguard_players:
                if p.hp <= 0: continue
                if random.random() < 0.2:
                    p.momentum = "Precision"
                    rearguard_players.append(p)
                    continue
                self.resolve_turn(p, party, self.enemies, forced_strategy=strategy)
            
            active_enemies = [e for e in self.enemies if e.hp > 0]
            random.shuffle(active_enemies)
            for e in active_enemies:
                if e.hp <= 0: continue
                self.resolve_turn(e, self.enemies, party)
            
            random.shuffle(rearguard_players)
            for p in rearguard_players:
                if p.hp <= 0 or p.has_acted: continue
                self.resolve_turn(p, party, self.enemies, forced_strategy=strategy)
                
        won = any(p.hp > 0 for p in party)
        hp_sum = sum(p.hp for p in party)
        max_hp_sum = sum(p.max_hp for p in party)
        hp_pct = hp_sum / max_hp_sum if max_hp_sum > 0 else 0
        killed = len([e for e in self.enemies if e.is_dead])
        van_pct = (vanguard_instances / total_instances) if total_instances > 0 else 0
        return EncounterResult(won, rounds, hp_pct, killed, total_enemies, van_pct)

    def resolve_turn(self, p: Character, friends: List[Character], foes: List[Character], forced_strategy: Optional[str] = None):
        strategy = forced_strategy if forced_strategy else "Default"
        attacks_made = 0
        
        while p.combat_ap > 0:
            if strategy == "SingleAttackLimit":
                if attacks_made >= 1:
                    # Forced to do something else: Move
                    p.moved_this_turn = 3
                    p.has_evasive_bonus = True
                    p.has_free_reaction = True
                    p.combat_ap -= 1
                    continue
                self.resolve_attack(p, friends, foes)
                attacks_made += 1
                p.combat_ap -= 1
                continue

            if strategy == "MoveAndAttack":
                if p.combat_ap == 2:
                    # Move 3m for Evasive bonus AND free reaction
                    p.moved_this_turn = 3
                    p.has_evasive_bonus = True
                    p.has_free_reaction = True
                    p.combat_ap -= 1
                    continue
                
                if attacks_made >= 1:
                    p.combat_ap = 0
                    continue

                self.resolve_attack(p, friends, foes)
                attacks_made += 1
                p.combat_ap -= 1
                continue
            
            if strategy == "DoubleAttack":
                self.resolve_attack(p, friends, foes)
                attacks_made += 1
                p.combat_ap -= 1
                continue

            # Default
            if p.hp < p.max_hp * 0.5 and p.moved_this_turn < 3 and p.combat_ap >= 1:
                p.moved_this_turn = 3
                p.has_evasive_bonus = True
                p.has_free_reaction = True
                p.combat_ap -= 1
                continue
            
            self.resolve_attack(p, friends, foes)
            p.combat_ap -= 1
        p.has_acted = True

    def resolve_attack(self, att: Character, friends: List[Character], foes: List[Character]):
        targets = [e for e in foes if e.hp > 0]
        if not targets: return
        vic = random.choice(targets)
        
        hit_mod = 0
        skill_val = att.skill_combat
        
        # Multiple Attack Penalty (MAP): Half Skill for 2nd attack
        if hasattr(att, 'attacks_this_turn') and att.attacks_this_turn >= 1:
            skill_val = skill_val // 2
        
        # Evasive Token Penalty: Retired (now handled by Defense bonus in take_damage)
        # if getattr(self, 'use_evasive_defense', False) and vic.moved_this_turn >= 3:
        #     hit_mod -= 20

        adv = att.next_attack_advantage
        if att.momentum == "Precision": adv = True
        if "Pack Tactics" in att.talents and any(f for f in friends if f.hp > 0 and f != att and (f.moved_this_turn > 0 or f.has_acted)):
            adv = True
        
        success, roll, dos, crit = att.roll_skill(skill_val, modifier=hit_mod, advantage=adv)
        
        if hasattr(att, 'attacks_this_turn'):
            att.attacks_this_turn += 1
        else:
            att.attacks_this_turn = 1

        if not success: return
        
        damage = att.weapon.damage + (att.skill_combat // 10 if crit else dos)
        
        # Momentum Bonus (Evasive Token): +2 damage if you moved 3m+
        if getattr(self, 'use_momentum_damage', False) and att.moved_this_turn >= 3:
            damage += 2
        if not crit and att.next_attack_overdrive: damage += dos

        dmg_reduction = 0
        final_dmg_mult = 1.0
        
        if vic.reactions > 0 or vic.has_free_reaction:
            if vic.has_free_reaction and getattr(self, 'use_free_reaction', False):
                vic.has_free_reaction = False # Use free reaction
            elif vic.reactions > 0:
                vic.reactions -= 1
            else:
                return # No reactions left and no free one used
                
            def_adv = vic.has_evasive_bonus or "Master of Defense" in vic.talents
            def_mod = 0
            
            if vic.offhand and vic.offhand.is_shield and "Blocker" in vic.talents:
                d_success, d_roll, d_dos, d_crit = vic.roll_skill(vic.skill_combat, modifier=def_mod, advantage=def_adv)
                if d_success: dmg_reduction = vic.offhand.defense + d_dos
                else: final_dmg_mult = 0.5
            elif "Dodge" in vic.talents:
                d_success, d_roll, d_dos, d_crit = vic.roll_skill(vic.stats.AGI, modifier=def_mod, advantage=def_adv)
                if d_success and d_dos >= 2: final_dmg_mult = 0.0
            elif "Parry" in vic.talents:
                d_success, d_roll, d_dos, d_crit = vic.roll_skill(vic.stats.AGI, modifier=def_mod, advantage=def_adv)
                if d_success: dmg_reduction = vic.weapon.damage + d_dos
            
        damage -= dmg_reduction
        vic.take_damage(int(max(0, damage * final_dmg_mult)))

def run_sim(name, party, enemies, iterations=100, strategy: Optional[str] = None):
    results = []
    for _ in range(iterations):
        for p in party: p.full_heal(); p.is_dead = False
        for e in enemies: e.full_heal(); e.is_dead = False
        enc = CombatEncounter(name, enemies)
        
        # Core Rules (Evasive Stance & Half-Skill MAP)
        enc.use_free_reaction = False
        enc.use_momentum_damage = False
        enc.use_evasive_defense = True
        
        results.append(enc.run(party, strategy=strategy))
    wins = [r for r in results if r.won]
    print(f"Encounter: {name} ({strategy if strategy else 'Default'})")
    print(f"  Win Rate: {len(wins) / iterations:.2%}")
    print(f"  Avg Rounds: {statistics.mean([r.rounds for r in results]):.1f}")
    print(f"  Avg Party HP: {statistics.mean([r.party_hp_pct for r in results]):.2%}")
    print("-" * 20)

def create_party():
    shield = Character("Shield", "Warrior", Stats(STR=70, CON=65, AGI=65, INS=40, LOG=60, CHA=60), heritage="Clansman")
    shield.weapon = Weapon("Long Sword", 7); shield.offhand = Weapon("Round Shield", 0, is_shield=True, defense=2)
    shield.armor = Armor("Chain Mail", 2); shield.skill_combat = 70; shield.ap = 20; shield.spend_ap()
    
    guide = Character("Guide", "Scout", Stats(AGI=70, CON=50, STR=50, INS=65, LOG=55, CHA=60), heritage="Farmer")
    guide.weapon = Weapon("Short Bow", 6, is_ranged=True); guide.armor = Armor("Leather", 1)
    guide.skill_combat = 70; guide.ap = 15; guide.spend_ap()
    
    seer = Character("Seer", "Mage", Stats(INS=75, LOG=70, AGI=65, CON=50, STR=50, CHA=50), heritage="Outcast")
    seer.weapon = Weapon("Dagger", 4); seer.armor = Armor("Clothes", 0)
    seer.skill_combat = 50; seer.ap = 10; seer.spend_ap()
    
    speaker = Character("Speaker", "Bard", Stats(CHA=70, AGI=65, INS=50, CON=60, STR=50, LOG=65), heritage="Noble")
    speaker.weapon = Weapon("Short Sword", 5); speaker.armor = Armor("Leather", 1)
    speaker.skill_combat = 65; speaker.ap = 15; speaker.spend_ap()
    return [shield, guide, seer, speaker]

def create_enemies(type_name, count):
    enemies = []
    for i in range(count):
        if type_name == "Wolf":
            e = Character(f"Wolf {i}", "Enemy", Stats(STR=40, AGI=60, CON=35, INS=25, LOG=15, CHA=10))
            e.weapon = Weapon("Bite", 1); e.armor = Armor("Fur", 1); e.skill_combat = 65
            e.max_hp = 12; e.hp = 12; e.max_reactions = 6; e.reactions = 6; e.talents = ["Pack Tactics"]
        elif type_name == "Bandit":
            e = Character(f"Bandit {i}", "Enemy", Stats(STR=50, AGI=50, CON=40, INS=30, LOG=40, CHA=40))
            e.weapon = Weapon("Long Sword", 7); e.armor = Armor("Leather", 1); e.skill_combat = 50
            e.max_hp = 15; e.hp = 15; e.max_reactions = 5; e.reactions = 5
        elif type_name == "Draugr":
            e = Character(f"Draugr {i}", "Enemy", Stats(STR=65, AGI=45, CON=55, INS=40, LOG=20, CHA=5))
            e.weapon = Weapon("Great Axe", 11); e.armor = Armor("Lamellar", 3); e.skill_combat = 55
            e.max_hp = 25; e.hp = 25; e.max_reactions = 4; e.reactions = 4
        enemies.append(e)
    return enemies

if __name__ == "__main__":
    party = create_party()
    scenarios = [
        ("Wolf Pack (8 Wolves)", create_enemies("Wolf", 8)),
        ("Bandit Ambush (8 Bandits)", create_enemies("Bandit", 8)),
        ("Draugr Crypt (4 Draugr)", create_enemies("Draugr", 4))
    ]
    for name, enemies in scenarios:
        print(f"--- {name} ---")
        run_sim(name, party, enemies, iterations=200, strategy="DoubleAttack")
        run_sim(name, party, enemies, iterations=200, strategy="MoveAndAttack")
