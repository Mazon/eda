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
    INT: int = 60
    MND: int = 60
    CHA: int = 60
    CON: int = 60

@dataclass
class Weapon:
    name: str
    damage: int
    is_ranged: bool = False
    hands: int = 1
    initiative_mod: int = 0
    is_shield: bool = False
    dr: int = 0 

@dataclass
class Armor:
    name: str
    dr: int = 0

@dataclass
class Character:
    name: str
    role: str
    stats: Stats
    hp: int = 0
    max_hp: int = 0
    mp: int = 0
    max_mp: int = 0
    reactions: int = 0
    max_reactions: int = 0
    nature: str = "The Wolf"
    heritage: str = "Hearth-born"
    
    weapon: Weapon = field(default_factory=lambda: Weapon("Fists", 3))
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
    cover_type: str = "None" # "None", "Light", "Heavy"
    is_hunkered: bool = False
    is_suppressed: bool = False
    moved_this_turn: int = 0
    has_evasive_bonus: bool = False
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
        hp_bonus = 10 if "Endurance Training" in self.talents else 0
        self.max_hp = self.stats.CON + hp_bonus
        self.max_mp = self.stats.MND // 4
        
        # Heritage Traits
        natural_dr = 0
        if self.heritage == "Blighted": natural_dr = 2
        self.natural_dr = natural_dr

        # Reactions Pool: (MND / 2) // 10
        self.max_reactions = (self.stats.MND // 2) // 10
        if "Duelist" in self.talents: self.max_reactions += 1
        
        # Ensure current reactions don't exceed new max
        if self.reactions > self.max_reactions: self.reactions = self.max_reactions

    def full_heal(self):
        if not self.is_dead:
            self.hp = self.max_hp
            self.mp = self.max_mp
            self.reactions = self.max_reactions

    def roll_skill(self, skill_val: int, skill_name: Optional[str] = None, modifier: int = 0, advantage: bool = False, disadvantage: bool = False) -> Tuple[bool, int, int, bool]:
        # Heritage: Umbral-kin Sun-Sick
        if self.heritage == "Umbral-kin" and getattr(self, "in_sunlight", False):
            modifier -= 10

        target = skill_val + modifier
        def do_roll():
            roll = random.randint(1, 100)
            if roll == 100: # Always fails
                return False, roll, 0
            success = roll <= target
            dos = roll // 10
            return success, roll, dos
        s1, r1, d1 = do_roll()
        if advantage and not disadvantage:
            s2, r2, d2 = do_roll()
            if r2 < r1: s1, r1, d1 = s2, r2, d2
        elif disadvantage and not advantage:
            s2, r2, d2 = do_roll()
            if r2 > r1: s1, r1, d1 = s2, r2, d2
        is_crit = s1 and r1 > 0 and r1 % 11 == 0
        if not s1 and r1 % 11 == 0 and skill_name:
            self.marked_skills.add(skill_name)
        return s1, r1, d1, is_crit

    def take_damage(self, amount: int):
        dr = self.armor.dr + getattr(self, "natural_dr", 0)
        if "Holy Aura" in self.talents: dr += 1
        if "Defensive Stance" in self.talents: dr += 2 # Adjusted to Rulebook
        if "Steel Resolve" in self.talents: dr += 2
        
        final_dmg = max(0, amount - dr)
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
        self.process_skill_marks()

    def process_skill_marks(self):
        for skill_name in list(self.marked_skills):
            pass
        self.marked_skills.clear()

    def spend_ap(self):
        while self.ap >= 5:
            added = False
            t1_options = ["Focus", "Overdrive", "Blocker", "Dodge", "First Strike", "Marked for Death", "Vanguard's Lead"]
            for t in t1_options:
                if t not in self.talents and self.ap >= 5:
                    self.talents.append(t); self.ap -= 5; self.recalc_derived(); added = True; break
            if added: continue
            
            t2_options = ["Guardian", "Cleave", "Holy Aura", "Tactical Guard", "Vengeful Retort", "Exploit Opening", "Harrying Strike", "Bloodied Fury", "Coordinated Assault", "Pack Tactics"]
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
    party_mp_pct: float
    enemies_killed: int
    total_enemies: int
    vanguard_percentage: float = 0.0

class CombatEncounter:
    def __init__(self, name: str, enemies: List[Character], is_boss=False):
        self.name, self.enemies, self.is_boss = name, enemies, is_boss
        
    def run(self, party: List[Character]) -> EncounterResult:
        rounds = 0
        total_enemies = len(self.enemies)
        vanguard_instances = 0
        total_instances = 0
        
        while any(p.hp > 0 for p in party) and any(e.hp > 0 for e in self.enemies):
            rounds += 1
            if rounds > 50: break
            
            # Start of Round Cleanup
            for c in party + self.enemies:
                c.combat_ap = 2
                c.next_attack_bonus_dmg = 0
                c.next_attack_advantage = False
                c.next_attack_overdrive = False
                c.is_hunkered = False
                c.moved_this_turn = 0
                c.has_evasive_bonus = False
                c.is_charging = False
                c.cannot_dodge = False
                if c.is_suppressed:
                    c.combat_ap -= 1
                    c.is_suppressed = False
                if "Vanguard Reflexes" in c.talents:
                    c.reactions = min(c.max_reactions, c.reactions + 1)
                else:
                    # Reactions do not refresh every round normally
                    pass
                c.momentum = None
                c.active_defense_bonus = 0
                c.is_marked = False
                c.has_disadvantage = False
                c.has_acted = False
                c.took_damage_this_round = False
                c.target_hit_this_round.clear()

            # Initiative
            vanguard_players = []
            rearguard_players = []
            for p in party:
                if p.hp <= 0: continue
                total_instances += 1
                mod = 0
                if "Tempo" in p.talents: mod += 10
                if "Battle Plan" in p.talents: mod += 10
                success, roll, dos, crit = p.roll_skill(p.stats.AGI, modifier=mod)
                if success: 
                    vanguard_players.append(p)
                    vanguard_instances += 1
                else: 
                    rearguard_players.append(p)
            
            # Vanguard Phase
            random.shuffle(vanguard_players)
            for p in vanguard_players:
                if p.hp <= 0: continue
                if random.random() < 0.2:
                    p.combat_ap -= 1
                    p.momentum = random.choice(["Precision", "Brace", "Observation"])
                    rearguard_players.append(p)
                    continue
                self.resolve_turn(p, party, self.enemies, phase="Vanguard")
            
            # Enemy Phase
            active_enemies = [e for e in self.enemies if e.hp > 0]
            random.shuffle(active_enemies)
            for e in active_enemies:
                if e.hp <= 0: continue
                self.resolve_turn(e, self.enemies, party, phase="Enemy")
            
            # Rearguard Phase
            random.shuffle(rearguard_players)
            for p in rearguard_players:
                if p.hp <= 0 or p.has_acted: continue
                self.resolve_turn(p, party, self.enemies, phase="Rearguard")
                
        won = any(p.hp > 0 for p in party)
        hp_sum = sum(p.hp for p in party)
        max_hp_sum = sum(p.max_hp for p in party)
        hp_pct = hp_sum / max_hp_sum if max_hp_sum > 0 else 0
        killed = len([e for e in self.enemies if e.is_dead])
        van_pct = (vanguard_instances / total_instances) if total_instances > 0 else 0
        return EncounterResult(won, rounds, hp_pct, 1.0, killed, total_enemies, van_pct)

    def resolve_turn(self, p: Character, friends: List[Character], foes: List[Character], phase: str):
        while p.combat_ap > 0:
            if "Focus" in p.talents and p.combat_ap >= 1 and not p.next_attack_advantage and random.random() < 0.3:
                p.next_attack_advantage = True
                p.combat_ap -= 1
                continue
            if "Overdrive" in p.talents and p.combat_ap >= 1 and not p.next_attack_overdrive and random.random() < 0.2:
                p.next_attack_overdrive = True
                p.combat_ap -= 1
                continue
            if p.combat_ap >= 1 and random.random() < 0.3:
                p.moved_this_turn = 5
                p.has_evasive_bonus = True
                p.combat_ap -= 1
                if phase == "Vanguard" and "Vanguard's Lead" in p.talents:
                    targets = [f for f in friends if f.hp > 0 and not f.has_acted]
                    if targets: random.choice(targets).momentum = "Precision"
                continue
            self.resolve_attack(p, friends, foes, phase=phase)
            p.combat_ap -= 1
        p.has_acted = True

    def resolve_attack(self, att: Character, friends: List[Character], foes: List[Character], phase: str):
        targets = [e for e in foes if e.hp > 0]
        if not targets: return
        vic = random.choice(targets)
        hit_mod = 0
        if att.momentum == "Precision": hit_mod += 5
        if att.weapon.is_ranged:
            if vic.cover_type == "Light": hit_mod -= 10
            elif vic.cover_type == "Heavy": hit_mod -= 20
            if "Calm Shooting" in att.talents:
                if vic.cover_type == "Light": hit_mod += 10
                elif vic.cover_type == "Heavy": hit_mod += 10
        adv = att.next_attack_advantage
        if "Pack Tactics" in att.talents and any(f for f in friends if f.hp > 0 and (f.moved_this_turn > 0 or f.has_acted)):
            adv = True
        success, roll, dos, crit = att.roll_skill(att.skill_combat, modifier=hit_mod, advantage=adv)
        if not success: return
        dmg_reduction = 0
        final_dmg_mult = 1.0
        if vic.reactions > 0 and not vic.cannot_dodge:
            vic.reactions -= 1
            def_adv = vic.momentum == "Observation" or "Master of Defense" in vic.talents
            def_mod = 0
            if vic.has_evasive_bonus: def_mod += 10
            if "Smart Fighting" in vic.talents and vic.cover_type != "None": def_mod += 10
            if vic.offhand and vic.offhand.is_shield and "Blocker" in vic.talents:
                d_success, d_roll, d_dos, d_crit = vic.roll_skill(vic.skill_combat, modifier=def_mod, advantage=def_adv)
                if d_success: dmg_reduction = vic.offhand.dr + d_dos
                else: final_dmg_mult = 0.5
            elif vic.stats.AGI > vic.skill_combat:
                d_success, d_roll, d_dos, d_crit = vic.roll_skill(vic.stats.AGI, modifier=def_mod, advantage=def_adv)
                if d_success: final_dmg_mult = 0.5
            else:
                d_success, d_roll, d_dos, d_crit = vic.roll_skill(vic.skill_combat, modifier=def_mod, advantage=def_adv)
                if d_success: dmg_reduction = vic.weapon.damage + d_dos
        if crit:
            damage = att.weapon.damage + (att.skill_combat // 10)
        else:
            damage = att.weapon.damage + dos
            if att.next_attack_overdrive: damage += dos
        damage -= dmg_reduction
        if phase == "Rearguard":
            if "First Strike" in att.talents: damage += 5
            if "Exploit Opening" in att.talents: damage += 10
        if vic.momentum == "Brace": damage -= 2
        vic.take_damage(int(max(0, damage * final_dmg_mult)))

def run_sim(name, party, enemies, iterations=100):
    results = []
    for _ in range(iterations):
        for p in party: p.full_heal(); p.is_dead = False
        for e in enemies: e.full_heal(); e.is_dead = False
        enc = CombatEncounter(name, enemies)
        results.append(enc.run(party))
    wins = [r for r in results if r.won]
    win_rate = len(wins) / iterations
    avg_rounds = statistics.mean([r.rounds for r in results])
    avg_hp = statistics.mean([r.party_hp_pct for r in results])
    print(f"Encounter: {name}")
    print(f"  Win Rate: {win_rate:.2%}")
    print(f"  Avg Rounds: {avg_rounds:.1f}")
    print(f"  Avg Party HP: {avg_hp:.2%}")
    print("-" * 20)

def create_party():
    shield = Character("Shield", "Warrior", Stats(STR=70, CON=65, AGI=60, MND=40), nature="The Bear", heritage="Hearth-born")
    shield.weapon = Weapon("Axe", 7)
    shield.offhand = Weapon("Shield", 0, is_shield=True, dr=2)
    shield.armor = Armor("Chain Mail", 2)
    shield.skill_combat = 70
    shield.ap = 30
    shield.spend_ap()
    guide = Character("Guide", "Scout", Stats(AGI=70, CON=50, STR=50, MND=60), nature="The Lynx", heritage="Wild-walker")
    guide.weapon = Weapon("Bow", 6, is_ranged=True)
    guide.armor = Armor("Leather", 1)
    guide.skill_combat = 70
    guide.ap = 20
    guide.spend_ap()
    seer = Character("Seer", "Mage", Stats(MND=75, INT=70, AGI=50, CON=50), nature="The Owl", heritage="Blighted")
    seer.weapon = Weapon("Staff", 4)
    seer.armor = Armor("Clothes", 0)
    seer.skill_combat = 50
    seer.ap = 10
    seer.spend_ap()
    speaker = Character("Speaker", "Bard", Stats(CHA=70, AGI=65, MND=50, CON=55), nature="The Fox", heritage="Hearth-born")
    speaker.weapon = Weapon("Rapier", 5)
    speaker.armor = Armor("Leather", 1)
    speaker.skill_combat = 65
    speaker.ap = 15
    speaker.spend_ap()
    return [shield, guide, seer, speaker]

def create_enemies(type_name, count):
    enemies = []
    for i in range(count):
        if type_name == "Wolf":
            e = Character(f"Wolf {i}", "Enemy", Stats(STR=40, AGI=60, CON=35, MND=25))
            e.weapon = Weapon("Bite", 5)
            e.armor = Armor("Fur", 1)
            e.skill_combat = 65
            e.talents = ["Pack Tactics"]
        elif type_name == "Bandit":
            e = Character(f"Bandit {i}", "Enemy", Stats(STR=50, AGI=50, CON=40, MND=30))
            e.weapon = Weapon("Sword", 7)
            e.armor = Armor("Leather", 2)
            e.skill_combat = 50
        elif type_name == "Draugr":
            e = Character(f"Draugr {i}", "Enemy", Stats(STR=65, AGI=45, CON=55, MND=40))
            e.weapon = Weapon("Axe", 10)
            e.armor = Armor("Plate", 3)
            e.skill_combat = 55
        enemies.append(e)
    return enemies

if __name__ == "__main__":
    party = create_party()
    run_sim("Wolf Pack (4 Wolves)", party, create_enemies("Wolf", 4))
    run_sim("Bandit Ambush (6 Bandits)", party, create_enemies("Bandit", 6))
    run_sim("Draugr Crypt (3 Draugr)", party, create_enemies("Draugr", 3))
