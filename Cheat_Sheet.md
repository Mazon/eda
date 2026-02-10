<style>
@page {
  size: A4;
  margin: 0;
}
html, body {
  margin: 0;
  padding: 0;
  width: 210mm;
  height: 297mm;
  font-family: 'Georgia', serif;
  font-size: 9pt; /* Slightly smaller for cheat sheet density */
  color: #1a1a1a;
  background-color: #ffffff;
  box-sizing: border-box;
}
* {
  box-sizing: border-box;
}

/* --- Layout Containers --- */
.page {
  width: 210mm;
  height: 296mm;
  padding: 10mm;
  position: relative;
  overflow: hidden;
  page-break-after: always;
  display: flex;
  flex-direction: column;
  gap: 8px;
}
.columns {
  display: flex;
  flex-direction: row;
  gap: 10mm;
  height: 100%;
}
.column {
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 8px;
}

/* --- Typography & Colors --- */
.primary-color { color: #8b0000; }
.bg-primary { background-color: #8b0000; color: white; }
.border-primary { border: 2px solid #8b0000; }

h1 {
  font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
  text-transform: uppercase;
  margin: 0;
  font-weight: bold;
  font-size: 18pt;
  letter-spacing: 2px;
  color: white;
}
h2 {
  font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
  text-transform: uppercase;
  margin: 0 0 4px 0;
  font-weight: bold;
  font-size: 10pt;
  color: white;
  background-color: #2c3e50;
  padding: 4px 8px;
  border-bottom: 2px solid #1a252f;
  border-radius: 2px;
}
h3 {
  font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
  font-size: 9pt;
  font-weight: bold;
  margin: 4px 0 2px 0;
  color: #8b0000;
  border-bottom: 1px solid #ddd;
}

.header-banner {
  background-color: #8b0000;
  padding: 8px 12px;
  display: flex;
  justify-content: center;
  align-items: center;
  border-radius: 4px;
  border-bottom: 2px solid #5a0000;
  margin-bottom: 4px;
}

table {
  width: 100%;
  border-collapse: collapse;
  font-size: 8pt;
  margin-bottom: 4px;
}
th, td {
  border: 1px solid #ddd;
  padding: 3px 4px;
  text-align: left;
  vertical-align: top;
}
th {
  background-color: #f2f2f2;
  font-weight: bold;
  font-family: 'Helvetica Neue', sans-serif;
}
tr:nth-child(even) {
  background-color: #f9f9f9;
}

.box {
  border: 1px solid #ccc;
  padding: 6px;
  border-radius: 4px;
  background-color: #fff;
}
ul {
  margin: 0;
  padding-left: 14px;
}
li {
  margin-bottom: 2px;
}
strong {
  color: #333;
}
.small-text {
  font-size: 8pt;
  color: #555;
  font-style: italic;
}
</style>

<div class="page">
  <div class="header-banner">
    <h1>Eda &mdash; Rules Cheat Sheet</h1>
  </div>

  <div class="columns">
    <!-- Left Column -->
    <div class="column">
      
      <div class="box">
        <h2>Core Mechanics</h2>
        <h3>Checks (d100)</h3>
        <ul>
            <li><strong>Success:</strong> Roll &le; Skill/Attribute.</li>
            <li><strong>Failure:</strong> Roll > Skill/Attribute.</li>
            <li><strong>Degree of Success (DoS):</strong> Tens digit of a successful roll (e.g., Roll 48 = 4 DoS).</li>
            <li><strong>Critical Success:</strong> Doubles under skill (11, 22, etc.).
                <ul>
                    <li><em>Combat:</em> Crit Dmg (Weapon + Tens) + <strong>Injury</strong>.</li>
                    <li><em>Non-Combat:</em> Auto success (max difficulty).</li>
                </ul>
            </li>
            <li><strong>Pushing:</strong> Gain Advantage, but lose 10 IP (Instinct).</li>
        </ul>

        <h3>Advantage & Disadvantage</h3>
        <ul>
            <li><strong>Advantage:</strong> Swap tens/units for best result.</li>
            <li><strong>Disadvantage:</strong> Swap tens/units for worst result.</li>
        </ul>

        <h3>Difficulty Modifiers</h3>
        <table>
            <tr><th>Difficulty</th><th>Requirement</th></tr>
            <tr><td>Easy</td><td>0 DoS (Routine tasks)</td></tr>
            <tr><td>Routine</td><td>1 DoS (Standard tasks)</td></tr>
            <tr><td>Challenge</td><td>2 DoS (Demanding tasks)</td></tr>
            <tr><td>Hard</td><td>4 DoS (Significant obstacles)</td></tr>
            <tr><td>Extreme</td><td>6 DoS (Edge of capability)</td></tr>
            <tr><td>Impossible</td><td>8 DoS (Legendary feats)</td></tr>
        </table>
      </div>

      <div class="box">
        <h2>Combat Actions</h2>
        <div class="small-text">Turn: 2 AP + 1 Zero Cost Action.</div>
        
        <h3>Standard Actions (1 AP)</h3>
        <ul>
            <li><strong>Move:</strong> Move up to Speed (AGI/10 m). <br><em>Evasive Stance:</em> Move >3m = +3 Defense.</li>
            <li><strong>Attack:</strong> Weapon check. 2nd attack = 1/2 skill.</li>
            <li><strong>Help:</strong> Advantage to ally (melee range).</li>
            <li><strong>Interact:</strong> Open door, light torch, etc.</li>
            <li><strong>Swap Weapon:</strong> Draw/Sheathe.</li>
            <li><strong>Stand Up:</strong> From prone.</li>
            <li><strong>Prepare:</strong> Save action for reaction later.</li>
        </ul>
        
        <h3>Zero Cost Actions</h3>
        <ul>
            <li><strong>Wait (Vanguard only):</strong> Drop to Rearguard. Regain 1 Reaction.</li>
        </ul>

        <h3>Reactions (Cost 1 Reaction from Pool)</h3>
        <ul>
            <li><strong>Dodge (AGI):</strong> Success = No damage.</li>
            <li><strong>Parry (Combat Style):</strong> Reduce dmg by Weapon + DoS.</li>
            <li><strong>Block (Shield):</strong> Reduce dmg by Shield + DoS. Fail = Half dmg.</li>
        </ul>
      </div>

      <div class="box">
        <h2>Damage & Wounds</h2>
        <ul>
            <li><strong>Damage:</strong> Weapon Base + DoS.</li>
            <li><strong>Bleeding:</strong> Take +1 dmg per stack from all hits. Removed by Medicine check.</li>
            <li><strong>Wounds/Injuries:</strong> Caused by Critical Hits. Roll on Injury Table.</li>
        </ul>
      </div>

    </div>

    <!-- Right Column -->
    <div class="column">
      
      <div class="box">
        <h2>Injury Table (d100)</h2>
        <table>
            <tr>
                <th style="width: 40px;">Roll</th>
                <th>Severity</th>
                <th>Effect & Description</th>
            </tr>
            <tr>
                <td>01-10</td>
                <td>Minor</td>
                <td><strong>Stunned:</strong> Lose next Half Action.<br><span class="small-text">Glancing Blow.</span></td>
            </tr>
            <tr>
                <td>11-20</td>
                <td>Minor</td>
                <td><strong>Pain:</strong> -10 to next check.<br><span class="small-text">Deep Gash.</span></td>
            </tr>
            <tr>
                <td>21-30</td>
                <td>Minor</td>
                <td><strong>Disoriented:</strong> Disadv. on Logic/Instinct (1d4 rnds).<br><span class="small-text">Knocked Senseless.</span></td>
            </tr>
            <tr>
                <td>31-40</td>
                <td>Mod.</td>
                <td><strong>Hobbled:</strong> Speed halved until healed.<br><span class="small-text">Leg Wound.</span></td>
            </tr>
            <tr>
                <td>41-50</td>
                <td>Mod.</td>
                <td><strong>Weakened Grip:</strong> Disadv. on arm checks.<br><span class="small-text">Arm Wound.</span></td>
            </tr>
            <tr>
                <td>51-60</td>
                <td>Mod.</td>
                <td><strong>Concussion:</strong> -10 Logic/Instinct permanently*.<br><span class="small-text">Head Trauma.</span></td>
            </tr>
            <tr>
                <td>61-70</td>
                <td>Severe</td>
                <td><strong>Winded:</strong> No "Sprint". -10 CON checks.<br><span class="small-text">Broken Ribs.</span></td>
            </tr>
            <tr>
                <td>71-80</td>
                <td>Severe</td>
                <td><strong>Vulnerable:</strong> Double dmg from Bleed stacks.<br><span class="small-text">Internal Injury.</span></td>
            </tr>
            <tr>
                <td>81-85</td>
                <td>Severe</td>
                <td><strong>Useless Limb:</strong> Limb unusable.<br><span class="small-text">Mangled Limb.</span></td>
            </tr>
            <tr>
                <td>86-90</td>
                <td>Severe</td>
                <td><strong>Permanent Loss:</strong> -5 to relevant stat.<br><span class="small-text">Severed Extremity.</span></td>
            </tr>
            <tr>
                <td>91-95</td>
                <td>Lethal</td>
                <td><strong>Dying:</strong> Drop to 0 HP.<br><span class="small-text">Mortal Wound.</span></td>
            </tr>
            <tr>
                <td>96-99</td>
                <td>Lethal</td>
                <td><strong>Amputation:</strong> Limb gone. CON check or pass out.<br><span class="small-text">Severed Limb.</span></td>
            </tr>
            <tr>
                <td>00</td>
                <td>Fatal</td>
                <td><strong>Dead:</strong> Instant death.<br><span class="small-text">Fatality.</span></td>
            </tr>
        </table>
        <div class="small-text" style="margin-top: 4px;">*Until fully rested/healed. Severe injuries require surgery.</div>
      </div>

      <div class="box">
        <h2>Conditions</h2>
        <table>
            <tr><th>Condition</th><th>Effect</th></tr>
            <tr><td><strong>Blinded</strong></td><td>Disadv. on attacks. Fail sight checks.</td></tr>
            <tr><td><strong>Frightened</strong></td><td>Disadv. on all checks. Can't move closer.</td></tr>
            <tr><td><strong>Prone</strong></td><td>Ranged attacks vs you: Disadv.<br>Melee attacks vs you: Adv.</td></tr>
            <tr><td><strong>Stunned</strong></td><td>No actions/reactions. Enemies have Adv.</td></tr>
            <tr><td><strong>Unconscious</strong></td><td>Prone & Stunned. Auto-fail checks. Crits vs you.</td></tr>
            <tr><td><strong>Exhaustion</strong></td><td>1: Disadv. checks. 2: Half speed. 3: Unconscious.</td></tr>
        </table>
      </div>

    </div>
  </div>
</div>
