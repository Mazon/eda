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
  font-size: 10pt;
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
  height: 296mm; /* slightly less to prevent overflow */
  padding: 12mm;
  position: relative;
  overflow: hidden;
  page-break-after: always;
  display: flex;
  flex-direction: column;
  gap: 10px;
}
.page:last-child {
  page-break-after: avoid;
}

/* --- Typography & Colors --- */
.primary-color { color: #8b0000; }
.bg-primary { background-color: #8b0000; color: white; }
.border-primary { border: 2px solid #8b0000; }

h1, h2, h3 {
  font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
  text-transform: uppercase;
  margin: 0;
  font-weight: bold;
}

.header-banner {
  background-color: #8b0000;
  color: white;
  padding: 8px 12px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  border-radius: 4px 4px 0 0;
  border-bottom: 2px solid #5a0000;
}
.header-banner h1 { font-size: 18pt; letter-spacing: 2px; }

.section-header {
  background-color: #2c3e50;
  color: white;
  padding: 4px 8px;
  font-size: 10pt;
  font-family: 'Helvetica Neue', sans-serif;
  text-transform: uppercase;
  letter-spacing: 1px;
  font-weight: bold;
  border-radius: 2px;
  margin-bottom: 5px;
  border-bottom: 2px solid #1a252f;
}

.label {
  font-size: 7pt;
  text-transform: uppercase;
  color: #555;
  font-family: 'Helvetica Neue', sans-serif;
  font-weight: bold;
  letter-spacing: 0.5px;
  margin-bottom: 2px;
  display: block;
}

/* --- Forms & Inputs --- */
input[type="text"], textarea {
  font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
  border: none;
  background: rgba(139, 0, 0, 0.03); /* Faint red tint */
  border-bottom: 1px solid #ccc;
  width: 100%;
  font-size: 11pt;
  padding: 2px 4px;
  color: #000;
  outline: none;
}
input[type="text"]:focus, textarea:focus {
  background: rgba(139, 0, 0, 0.08);
  border-bottom: 1px solid #8b0000;
}
textarea {
  resize: none;
  height: 100%;
  border: 1px solid #eee; /* Box for text areas */
  padding: 5px;
}

.box-input {
  border: 2px solid #8b0000;
  height: 40px;
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  background: white;
  border-radius: 4px;
}
.box-input input {
  text-align: center;
  font-size: 16pt;
  font-weight: bold;
  height: 100%;
  background: transparent;
  border: none;
  width: 100%;
}

.checkbox-wrapper {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 20px;
  height: 20px;
  border: 1px solid #8b0000;
  border-radius: 50%; /* Circle for skills */
  background: white;
}
.checkbox-wrapper input {
  width: 14px;
  height: 14px;
  margin: 0;
  cursor: pointer;
  accent-color: #8b0000;
}

/* --- Specific Components --- */
.top-info-grid {
  display: grid;
  grid-template-columns: 2fr 1.5fr 0.5fr;
  gap: 15px;
  padding: 10px;
  border: 2px solid #8b0000;
  border-top: none;
  background: #fdfaf3;
  margin-bottom: 15px;
}
.field-group { display: flex; flex-direction: column; }

.main-columns {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 15px;
  flex: 1; /* Fill remaining space */
}

/* Attributes Table */
.attributes-container {
  border: 1px solid #ccc;
  padding: 5px;
}
.attribute-row {
  display: grid;
  grid-template-columns: 1fr 50px;
  gap: 10px;
  align-items: center;
  margin-bottom: 8px;
  background: #f9f9f9;
  padding: 5px;
  border-radius: 4px;
  border: 1px solid #eee;
}
.attribute-name {
  font-weight: bold;
  font-size: 11pt;
  color: #8b0000;
  display: flex;
  flex-direction: column;
}
.attribute-abbr {
  font-size: 8pt;
  color: #555;
}

/* Vitality Grid */
.vitality-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 10px;
}
.stat-box {
  border: 1px solid #ccc;
  padding: 5px;
  text-align: center;
  background: #fdfaf3;
}
.stat-box input { text-align: center; font-weight: bold; }

/* Weapons Table */
.weapons-table {
  width: 100%;
  border-collapse: collapse;
  font-size: 9pt;
}
.weapons-table th {
  background: #ddd;
  padding: 4px;
  text-align: left;
  font-size: 8pt;
  border: 1px solid #bbb;
}
.weapons-table td {
  border: 1px solid #ccc;
  padding: 0;
  height: 30px;
}
.weapons-table input {
  height: 100%;
  border: none;
  background: transparent;
  padding: 0 5px;
}

/* Skills Grid (Page 2) */
.skills-container {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 20px;
}
.skill-category {
  margin-bottom: 10px;
}
.skill-row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 4px 0;
  border-bottom: 1px dotted #ccc;
}
.skill-name {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 9.5pt;
  font-weight: bold;
}
.skill-stat {
  font-size: 8pt;
  color: #666;
  margin-left: 4px;
}
.skill-val {
  width: 40px;
  border-bottom: 1px solid #8b0000;
}
.skill-val input {
  text-align: center;
  font-weight: bold;
  background: transparent;
  border: none;
}

/* Inventory */
.inventory-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 5px;
}
.inv-slot {
  border-bottom: 1px solid #ccc;
  height: 24px;
}
.inv-slot input { height: 100%; border: none; background: transparent; }

/* Currency */
.currency-bar {
  display: flex;
  justify-content: space-around;
  background: #fdfaf3;
  border: 1px solid #e0e0e0;
  padding: 8px;
  margin-top: 5px;
  border-radius: 4px;
}
.coin-input {
  display: flex;
  align-items: center;
  gap: 5px;
  font-weight: bold;
  color: #8b0000;
}
.coin-input input {
  width: 60px;
  text-align: center;
  border-bottom: 2px solid #8b0000;
}

</style>

<!-- PAGE 1 -->
<div class="page">
  
  <div class="header-banner">
    <h1>CHARACTER RECORD</h1>
    <div style="font-size: 9pt; opacity: 0.8;">EDA RPG</div>
  </div>

  <div class="top-info-grid">
    <div class="field-group">
      <span class="label">Character Name</span>
      <input type="text" name="char_name" style="font-size: 14pt; font-weight: bold;">
    </div>
    <div class="field-group">
      <span class="label">Lineage & Heritage</span>
      <input type="text" name="lineage">
    </div>
    <div class="field-group">
      <span class="label">Total XP</span>
      <div class="box-input" style="height: 30px;">
        <input type="text" name="xp">
      </div>
    </div>
  </div>

  <div class="main-columns">
    <!-- LEFT COLUMN PAGE 1 -->
    <div style="display: flex; flex-direction: column; gap: 10px;">
      <!-- ATTRIBUTES -->
      <div>
        <div class="section-header">Attributes</div>
        <div class="attributes-container">
          <div class="attribute-row">
            <div class="attribute-name">STRENGTH <span class="attribute-abbr">STR</span></div>
            <div class="box-input"><input type="text" name="attr_str"></div>
          </div>
          <div class="attribute-row">
            <div class="attribute-name">AGILITY <span class="attribute-abbr">AGI</span></div>
            <div class="box-input"><input type="text" name="attr_agi"></div>
          </div>
          <div class="attribute-row">
            <div class="attribute-name">LOGIC <span class="attribute-abbr">LOG</span></div>
            <div class="box-input"><input type="text" name="attr_log"></div>
          </div>
          <div class="attribute-row">
            <div class="attribute-name">INSTINCT <span class="attribute-abbr">INS</span></div>
            <div class="box-input"><input type="text" name="attr_ins"></div>
          </div>
          <div class="attribute-row">
            <div class="attribute-name">CHARISMA <span class="attribute-abbr">CHA</span></div>
            <div class="box-input"><input type="text" name="attr_cha"></div>
          </div>
          <div class="attribute-row">
            <div class="attribute-name">CONSTITUTION <span class="attribute-abbr">CON</span></div>
            <div class="box-input"><input type="text" name="attr_con"></div>
          </div>
        </div>
      </div>
      <!-- TALENTS -->
      <div style="flex: 1; display: flex; flex-direction: column;">
        <div class="section-header">Talents & Abilities</div>
        <div style="border: 1px solid #ccc; padding: 5px; background: #fdfaf3; margin-bottom: 5px;">
           <span class="label">Heritage Traits</span>
           <input type="text" name="heritage_traits">
        </div>
        <table class="weapons-table" style="flex: 1;">
          <tr style="height: 20px;">
            <th width="10%" style="text-align: center;">Tier</th>
            <th width="30%">Name</th>
            <th width="60%">Effect</th>
          </tr>
          <tr>
            <td><input type="text" style="text-align: center;"></td>
            <td><input type="text"></td>
            <td><input type="text"></td>
          </tr>
           <tr>
            <td><input type="text" style="text-align: center;"></td>
            <td><input type="text"></td>
            <td><input type="text"></td>
          </tr>
           <tr>
            <td><input type="text" style="text-align: center;"></td>
            <td><input type="text"></td>
            <td><input type="text"></td>
          </tr>
           <tr>
            <td><input type="text" style="text-align: center;"></td>
            <td><input type="text"></td>
            <td><input type="text"></td>
          </tr>
           <tr>
            <td><input type="text" style="text-align: center;"></td>
            <td><input type="text"></td>
            <td><input type="text"></td>
          </tr>
           <tr>
            <td><input type="text" style="text-align: center;"></td>
            <td><input type="text"></td>
            <td><input type="text"></td>
          </tr>
           <tr>
            <td><input type="text" style="text-align: center;"></td>
            <td><input type="text"></td>
            <td><input type="text"></td>
          </tr>
        </table>
      </div>
    </div>
    <!-- RIGHT COLUMN PAGE 1 -->
    <div style="display: flex; flex-direction: column; gap: 10px;">
      <!-- VITALITY -->
      <div>
        <div class="section-header">Vitality & Defense</div>
        <div class="vitality-grid">
           <div class="stat-box">
             <span class="label">Health Points (HP)</span>
             <div style="display: flex; gap: 5px;">
               <input type="text" placeholder="Cur"> <span style="font-size:14pt;">/</span> <input type="text" placeholder="Max">
             </div>
           </div>
           <div class="stat-box">
             <span class="label">Instinct Points (IP)</span>
             <div style="display: flex; gap: 5px;">
               <input type="text" placeholder="Cur"> <span style="font-size:14pt;">/</span> <input type="text" placeholder="Max">
             </div>
           </div>
           <div class="stat-box">
             <span class="label">Speed</span>
             <div class="box-input" style="height: 35px; border: none; border-bottom: 2px solid #8b0000; border-radius: 0;">
                <input type="text" name="speed">
             </div>
           </div>
            <div class="stat-box">
             <span class="label">Defense</span>
             <div class="box-input" style="height: 35px; border: none; border-bottom: 2px solid #8b0000; border-radius: 0;">
                <input type="text" name="defense">
             </div>
           </div>
        </div>
        <div style="display: grid; grid-template-columns: 1fr 2fr; gap: 10px; margin-top: 10px;">
            <div class="stat-box">
                 <span class="label">Reaction Pool</span>
                 <input type="text" name="reaction">
            </div>
            <div class="stat-box">
                 <span class="label">Wound Clock</span>
                 <div style="display: flex; gap: 5px; justify-content: center; margin: 2px 0;">
                     <div class="checkbox-wrapper"><input type="checkbox"></div>
                     <div class="checkbox-wrapper"><input type="checkbox"></div>
                     <div class="checkbox-wrapper"><input type="checkbox"></div>
                     <div class="checkbox-wrapper"><input type="checkbox"></div>
                 </div>
                 <input type="text" name="wounds" placeholder="List injuries..." style="font-size: 9pt; text-align: center;">
            </div>
        </div>
      </div>
      <!-- ARSENAL -->
      <div>
        <div class="section-header">Arsenal & Combat</div>
        <table class="weapons-table">
          <tr>
            <th width="35%">Weapon</th>
            <th width="15%" style="text-align: center;">Mod</th>
            <th width="15%" style="text-align: center;">Dmg</th>
            <th width="35%">Notes</th>
          </tr>
          <tr>
             <td><input type="text"></td>
             <td><input type="text" style="text-align: center;"></td>
             <td><input type="text" style="text-align: center;"></td>
             <td><input type="text"></td>
          </tr>
          <tr>
             <td><input type="text"></td>
             <td><input type="text" style="text-align: center;"></td>
             <td><input type="text" style="text-align: center;"></td>
             <td><input type="text"></td>
          </tr>
          <tr>
             <td><input type="text"></td>
             <td><input type="text" style="text-align: center;"></td>
             <td><input type="text" style="text-align: center;"></td>
             <td><input type="text"></td>
          </tr>
          <tr>
             <td><input type="text"></td>
             <td><input type="text" style="text-align: center;"></td>
             <td><input type="text" style="text-align: center;"></td>
             <td><input type="text"></td>
          </tr>
        </table>
      </div>
       <!-- CONDITIONS / NOTES FILLER -->
      <div style="flex: 1; display: flex; flex-direction: column;">
        <div class="section-header">Active Conditions</div>
        <textarea style="flex: 1; background: #fdfaf3;"></textarea>
      </div>
    </div>
  </div>
</div>


<!-- PAGE 2 -->
<div class="page">
  <div class="header-banner">
    <h1>PROFICIENCIES & INVENTORY</h1>
  </div>

  <div class="main-columns" style="height: 100%;">
    <!-- LEFT COLUMN PAGE 2: SKILLS -->
    <div>
      <div class="section-header">Skills</div>
      <div style="font-size: 8pt; color: #666; margin-bottom: 5px; text-align: center; font-style: italic;">Check box if Trained.</div> 
      <div class="skills-container" style="display: block;">
        <!-- Physical Skills -->
        <div class="skill-category">
          <div style="border-bottom: 1px solid #8b0000; color: #8b0000; font-weight: bold; font-size: 9pt; margin-bottom: 5px;">PHYSICAL & AGILITY</div>
          <div class="skill-row">
            <div class="skill-name">
              <div class="checkbox-wrapper"><input type="checkbox" name="skill_acrobatics"></div>
              Acrobatics <span class="skill-stat">(AGI)</span>
            </div>
            <div class="skill-val"><input type="text"></div>
          </div>
          <div class="skill-row">
            <div class="skill-name">
              <div class="checkbox-wrapper"><input type="checkbox" name="skill_athletics"></div>
              Athletics <span class="skill-stat">(STR)</span>
            </div>
            <div class="skill-val"><input type="text"></div>
          </div>
           <div class="skill-row">
            <div class="skill-name">
              <div class="checkbox-wrapper"><input type="checkbox" name="skill_drive"></div>
              Drive Vehicle <span class="skill-stat">(AGI)</span>
            </div>
            <div class="skill-val"><input type="text"></div>
          </div>
           <div class="skill-row">
            <div class="skill-name">
              <div class="checkbox-wrapper"><input type="checkbox" name="skill_riding"></div>
              Riding <span class="skill-stat">(AGI)</span>
            </div>
            <div class="skill-val"><input type="text"></div>
          </div>
           <div class="skill-row">
            <div class="skill-name">
              <div class="checkbox-wrapper"><input type="checkbox" name="skill_stealth"></div>
              Stealth <span class="skill-stat">(AGI)</span>
            </div>
            <div class="skill-val"><input type="text"></div>
          </div>
           <div class="skill-row">
            <div class="skill-name">
              <div class="checkbox-wrapper"><input type="checkbox" name="skill_thievery"></div>
              Thievery <span class="skill-stat">(AGI)</span>
            </div>
            <div class="skill-val"><input type="text"></div>
          </div>
        </div>
        <!-- Social Skills -->
        <div class="skill-category" style="margin-top: 15px;">
          <div style="border-bottom: 1px solid #8b0000; color: #8b0000; font-weight: bold; font-size: 9pt; margin-bottom: 5px;">SOCIAL & CHARISMA</div>
          <div class="skill-row">
            <div class="skill-name">
              <div class="checkbox-wrapper"><input type="checkbox" name="skill_animal"></div>
              Animal Training <span class="skill-stat">(CHA)</span>
            </div>
            <div class="skill-val"><input type="text"></div>
          </div>
          <div class="skill-row">
            <div class="skill-name">
              <div class="checkbox-wrapper"><input type="checkbox" name="skill_barter"></div>
              Barter <span class="skill-stat">(CHA)</span>
            </div>
            <div class="skill-val"><input type="text"></div>
          </div>
           <div class="skill-row">
            <div class="skill-name">
              <div class="checkbox-wrapper"><input type="checkbox" name="skill_bluff"></div>
              Bluff <span class="skill-stat">(CHA)</span>
            </div>
            <div class="skill-val"><input type="text"></div>
          </div>
           <div class="skill-row">
            <div class="skill-name">
              <div class="checkbox-wrapper"><input type="checkbox" name="skill_diplomacy"></div>
              Diplomacy <span class="skill-stat">(CHA)</span>
            </div>
            <div class="skill-val"><input type="text"></div>
          </div>
           <div class="skill-row">
            <div class="skill-name">
              <div class="checkbox-wrapper"><input type="checkbox" name="skill_entertain"></div>
              Entertain <span class="skill-stat">(CHA)</span>
            </div>
            <div class="skill-val"><input type="text"></div>
          </div>
           <div class="skill-row">
            <div class="skill-name">
              <div class="checkbox-wrapper"><input type="checkbox" name="skill_intimidate"></div>
              Intimidate <span class="skill-stat">(CHA)</span>
            </div>
            <div class="skill-val"><input type="text"></div>
          </div>
           <div class="skill-row">
            <div class="skill-name">
              <div class="checkbox-wrapper"><input type="checkbox" name="skill_persuade"></div>
              Persuade <span class="skill-stat">(CHA)</span>
            </div>
            <div class="skill-val"><input type="text"></div>
          </div>
        </div>
        <!-- Mental Skills -->
        <div class="skill-category" style="margin-top: 15px;">
          <div style="border-bottom: 1px solid #8b0000; color: #8b0000; font-weight: bold; font-size: 9pt; margin-bottom: 5px;">MENTAL & KNOWLEDGE</div>
          <div class="skill-row">
            <div class="skill-name">
              <div class="checkbox-wrapper"><input type="checkbox" name="skill_alchemy"></div>
              Alchemy <span class="skill-stat">(LOG)</span>
            </div>
            <div class="skill-val"><input type="text"></div>
          </div>
          <div class="skill-row">
            <div class="skill-name">
              <div class="checkbox-wrapper"><input type="checkbox" name="skill_appraise"></div>
              Appraise <span class="skill-stat">(LOG)</span>
            </div>
            <div class="skill-val"><input type="text"></div>
          </div>
           <div class="skill-row">
            <div class="skill-name">
              <div class="checkbox-wrapper"><input type="checkbox" name="skill_crafting"></div>
              Crafting <span class="skill-stat">(LOG)</span>
            </div>
            <div class="skill-val"><input type="text"></div>
          </div>
           <div class="skill-row">
            <div class="skill-name">
              <div class="checkbox-wrapper"><input type="checkbox" name="skill_disguise"></div>
              Disguise <span class="skill-stat">(LOG)</span>
            </div>
            <div class="skill-val"><input type="text"></div>
          </div>
           <div class="skill-row">
            <div class="skill-name">
              <div class="checkbox-wrapper"><input type="checkbox" name="skill_engineering"></div>
              Engineering <span class="skill-stat">(LOG)</span>
            </div>
            <div class="skill-val"><input type="text"></div>
          </div>
           <div class="skill-row">
            <div class="skill-name">
              <div class="checkbox-wrapper"><input type="checkbox" name="skill_history"></div>
              History <span class="skill-stat">(LOG)</span>
            </div>
            <div class="skill-val"><input type="text"></div>
          </div>
           <div class="skill-row">
            <div class="skill-name">
              <div class="checkbox-wrapper"><input type="checkbox" name="skill_investigation"></div>
              Investigation <span class="skill-stat">(LOG)</span>
            </div>
            <div class="skill-val"><input type="text"></div>
          </div>
           <div class="skill-row">
            <div class="skill-name">
              <div class="checkbox-wrapper"><input type="checkbox" name="skill_linguistics"></div>
              Linguistics <span class="skill-stat">(LOG)</span>
            </div>
            <div class="skill-val"><input type="text"></div>
          </div>
           <div class="skill-row">
            <div class="skill-name">
              <div class="checkbox-wrapper"><input type="checkbox" name="skill_medicine"></div>
              Medicine <span class="skill-stat">(LOG)</span>
            </div>
            <div class="skill-val"><input type="text"></div>
          </div>
           <div class="skill-row">
            <div class="skill-name">
              <div class="checkbox-wrapper"><input type="checkbox" name="skill_nature"></div>
              Nature <span class="skill-stat">(LOG)</span>
            </div>
            <div class="skill-val"><input type="text"></div>
          </div>
           <div class="skill-row">
            <div class="skill-name">
              <div class="checkbox-wrapper"><input type="checkbox" name="skill_navigation"></div>
              Navigation <span class="skill-stat">(LOG)</span>
            </div>
            <div class="skill-val"><input type="text"></div>
          </div>
           <div class="skill-row">
            <div class="skill-name">
              <div class="checkbox-wrapper"><input type="checkbox" name="skill_occult"></div>
              Occult Knowledge <span class="skill-stat">(LOG)</span>
            </div>
            <div class="skill-val"><input type="text"></div>
          </div>s
           <div class="skill-row">
            <div class="skill-name">
              <div class="checkbox-wrapper"><input type="checkbox" name="skill_perception"></div>
              Perception <span class="skill-stat">(INS)</span>
            </div>
            <div class="skill-val"><input type="text"></div>
          </div>
           <div class="skill-row">
            <div class="skill-name">
              <div class="checkbox-wrapper"><input type="checkbox" name="skill_religion"></div>
              Religion <span class="skill-stat">(LOG)</span>
            </div>
            <div class="skill-val"><input type="text"></div>
          </div>
           <div class="skill-row">
            <div class="skill-name">
              <div class="checkbox-wrapper"><input type="checkbox" name="skill_seafaring"></div>
              Seafaring <span class="skill-stat">(LOG)</span>
            </div>
            <div class="skill-val"><input type="text"></div>
          </div>
           <div class="skill-row">
            <div class="skill-name">
              <div class="checkbox-wrapper"><input type="checkbox" name="skill_survival"></div>
              Survival <span class="skill-stat">(CON)</span>
            </div>
            <div class="skill-val"><input type="text"></div>
          </div>
           <div class="skill-row">
            <div class="skill-name">
              <div class="checkbox-wrapper"><input type="checkbox" name="skill_tracking"></div>
              Tracking <span class="skill-stat">(LOG)</span>
            </div>
            <div class="skill-val"><input type="text"></div>
          </div>
           <div class="skill-row">
            <div class="skill-name">
              <div class="checkbox-wrapper"><input type="checkbox" name="skill_warfare"></div>
              Warfare <span class="skill-stat">(LOG)</span>
            </div>
            <div class="skill-val"><input type="text"></div>
          </div>
        </div>
      </div>
    </div>
    <!-- RIGHT COLUMN PAGE 2: INVENTORY & BIO -->
    <div style="display: flex; flex-direction: column; gap: 15px;">
      <!-- EQUIPMENT -->
      <div>
        <div class="section-header">Equipment & Wealth</div>
        <div style="border: 2px solid #ccc; padding: 10px; background: #fff; min-height: 250px;">
          <span class="label">Inventory</span>
          <div class="inventory-grid">
            <div class="inv-slot"><input type="text"></div><div class="inv-slot"><input type="text"></div>
            <div class="inv-slot"><input type="text"></div><div class="inv-slot"><input type="text"></div>
            <div class="inv-slot"><input type="text"></div><div class="inv-slot"><input type="text"></div>
            <div class="inv-slot"><input type="text"></div><div class="inv-slot"><input type="text"></div>
            <div class="inv-slot"><input type="text"></div><div class="inv-slot"><input type="text"></div>
            <div class="inv-slot"><input type="text"></div><div class="inv-slot"><input type="text"></div>
            <div class="inv-slot"><input type="text"></div><div class="inv-slot"><input type="text"></div>
            <div class="inv-slot"><input type="text"></div><div class="inv-slot"><input type="text"></div>
            <div class="inv-slot"><input type="text"></div><div class="inv-slot"><input type="text"></div>
            <div class="inv-slot"><input type="text"></div><div class="inv-slot"><input type="text"></div>
            <div class="inv-slot"><input type="text"></div><div class="inv-slot"><input type="text"></div>
             <div class="inv-slot"><input type="text"></div><div class="inv-slot"><input type="text"></div>
             <div class="inv-slot"><input type="text"></div><div class="inv-slot"><input type="text"></div>
          </div>
        </div>
        <div class="currency-bar">
          <div class="coin-input">GP <input type="text"></div>
          <div class="coin-input" style="color: #666;">SP <input type="text" style="border-color: #666;"></div>
          <div class="coin-input" style="color: #a86b32;">CP <input type="text" style="border-color: #a86b32;"></div>
        </div>
      </div>
      <!-- BIOGRAPHY -->
      <div style="flex: 1; display: flex; flex-direction: column;">
        <div class="section-header">Biography</div>
        <div style="flex: 1; display: flex; flex-direction: column; gap: 10px;">
          <div style="flex: 1; border: 1px solid #ccc; padding: 5px; background: #fdfaf3;">
             <span class="label">Backstory & Origins</span>
             <textarea></textarea>
          </div>
          <div style="flex: 1; border: 1px solid #ccc; padding: 5px; background: #fdfaf3;">
             <span class="label">Allies, Rivals & Notes</span>
             <textarea></textarea>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
