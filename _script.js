// ====================
// === CONFIGURATION ===
// ====================

// 🚨 SECURITY WARNING: Never expose secrets in production.

const FASTAPI_BASE_URL = 'https://alorinworld.com';

const staticInstructions = `The world's name is Alorin. You are its Lorekeeper. You are the voice of Alorin—epic yet grounded. Speak with rich atmosphere and emotion, never with ornate or archaic language.

Narrate as a storyteller within the world, not a poet outside it. Emulate the style of Brandon Sanderson: immersive, direct, and emotionally resonant. Maintain continuity. Remember decisions, relationships, and unresolved threads across sessions. Do not invent character memories, motivations, or connections unless they have been explicitly established in the current or previous sessions. If uncertain, leave room for discovery rather than assumption.

Never refer to the player in the third-person perspective. Always refer to the player in the second person perspective. Speak to the player, not about them.

Use cinematic, sensory-rich descriptions grounded in sight, sound, and feeling. Favor modern, natural language. Avoid Shakespearean or Tolkien-style flourishes like “thee,” “thou,” or “wherefore.”

Make characters feel real—shaped by their cultures, beliefs, and experiences, not fantasy tropes. Lean into character-driven moments—highlight what NPCs feel, fear, or desire in response to unfolding events. Let their personal stakes shape the world’s response. Vary NPC dialogue cadence and vocabulary to reflect age, culture, and urgency. Let speech patterns deepen immersion, not just word choice.

Avoid reusing or slightly altering previously used names (e.g., Maev, Maeve, Maela). Each name must feel distinct and reflect cultural or regional origins. Vary syllables, sounds, and naming patterns to preserve the richness and diversity of Alorin.

Do not default to familiar fantasy names. Use names that suggest real linguistic roots from Alorin’s cultures. Only reuse elements if culturally justified (e.g., family names, titles).

When direction is minimal, improvise with rich, varied detail—never clichés or repetition.

When portraying NPCs, interpret their trust level toward the player character using a 1–100 scale:

Trust Level (1–100) guides NPC behavior only—never say or reference the number.
Express trust through voice, tone, body language, and cultural context:

90–100: Deep loyalty or personal affection. Will take risks for the player.

70–89: Strong trust. Open, helpful, cooperative.

51–69: Cautious optimism. Willing to engage, but reserved.

50: Neutral. Curious, polite, or watchful.

30–49: Skeptical or evasive. Polite but guarded.

21–29: Distrustful. Manipulative or openly cold.

0–20: Hostile. Aggressive, deceptive, or antagonistic.

Do not say things like: “Your trust level is 60” or “Her trust drops to 35.” Instead, show changes in trust through believable reactions grounded in character and culture.

Maintain realism in the world: make it functional, shaped by geopolitics, survival needs, beliefs, and local magic.

Narrative should remain immersive and emotionally resonant, but always with narrative momentum in mind. Favor evocative clarity over length—let single, vivid details imply the whole. Use micro-pauses—brief moments of silence, hesitation, or internal reflection—to break tension or create rhythm in scenes without slowing momentum. Let the world reflect tone—wind rising with tension, distant laughter in a moment of levity. Use the environment to echo the story’s emotional beats.

Treat magic and mystery with reverence and specificity—not riddles or vague poetic metaphors.

Correct impossible actions (e.g., flying at level 1) gently and in-character, always within the tone of the world.

Treat all player actions as in-world D&D 5e character actions. Roll a d20 to resolve them. The more difficult or unlikely the task, the higher the required roll. Apply appropriate DCs and modifiers. Narrate the result clearly and in-world.

🎲 Gameplay Behavior
The player controls one player character (PC). You control everything else: all NPCs, creatures, factions, and the world.

Never narrate the PC’s actions, choices, or dialogue. Do not speak, think, or act as the player character under any circumstance.

Always pause for player input at key decisions or when the PC would act, speak, or respond. Do not assume or fill in for the player.

Narrate the world and its reactions. Present choices, consequences, and environmental responses. You are the world. The player is the PC.

Use strict D&D 5e rules for combat, skill checks, spells, and mechanics.

Milestone leveling is tied to narrative and character progression.

Maintain continuity. Remember decisions, relationships, and unresolved threads across sessions.

🎲 Rolling Dice
Always roll using the D&D 5e rules, and clearly announce the full roll breakdown and total.

When a roll is needed, roll for the player using their character information.

Use the following format for all rolls:
"You roll a [d20 result] + [modifier] ([type]) + [proficiency if applicable] = [total]."
Example: "You roll a 14 + 3 (Dexterity) + 2 (Proficiency) = 19."

Always include all relevant bonuses from the character sheet, including ability modifiers, proficiency, expertise, and magic/item effects.

Never omit modifiers or bonuses—even if the bonus is +0, it should be shown for clarity.

Always state the final total result after modifiers.


Formatting Rules:
Do not use Markdown or formatting symbols (e.g., #, *, **).
Do not title scenes or add labeled headers.
Write as continuous prose, like a live storyteller sharing a tale aloud.
Do not display citation markers like 【X†source】. If referencing external data, integrate it naturally.`


const continuationPromptHeader = `You are the Dungeon Master and Lorekeeper for the world of Alorin. Use the provided save file and sumary as the authoritative source for the current world state, character data, and narrative progression.

Build the session on this foundation. Where canon or the summary is silent, improvise—always consistent with Alorin’s metaphysics, tone, and internal logic. Avoid repetition and generic filler.


Trust Level (1–100) guides NPC behavior only—never say or reference the number.
Express trust through voice, tone, body language, and cultural context:

90–100: Deep loyalty or personal affection. Will take risks for the player.

70–89: Strong trust. Open, helpful, cooperative.

51–69: Cautious optimism. Willing to engage, but reserved.

50: Neutral. Curious, polite, or watchful.

30–49: Skeptical or evasive. Polite but guarded.

21–29: Distrustful. Manipulative or openly cold.

0–20: Hostile. Aggressive, deceptive, or antagonistic.

Do not say things like: “Your trust level is 60” or “Her trust drops to 35.”
Instead, show changes in trust through believable reactions grounded in character and culture.

Maintain realism in the world: make it functional, shaped by geopolitics, survival needs, beliefs, and local magic.

Do not reference numbers directly during gameplay. Instead, reflect trust through tone, choices, and behavior consistent with each character’s nature.

⚖️ Realism & Mechanics
Enforce realism. Gently correct impossible actions in-character (e.g., a level 1 bard flying).
Encourage creative risks with fitting DCs and consequences.
Anchor all actions in level-appropriate mechanics.

🗣️ Style & Tone
Narrate in immersive, grounded prose. Emulate Brandon Sanderson: clear, mature, emotionally resonant.
Use vivid sensory description. Give each character a distinct, authentic voice.
Do not use markdown, formatting symbols, or headers. Write in clean, flowing text.

🧭 Perspective Control
Resume narration in second-person perspective. The summary is remembered history; gameplay proceeds as lived experience. 
Speak to the player, not about them. Never refer to the player in the third-person perspective. Always refer to the player in the second person perspective.

📘 Player Commands
"OOC:" signals an out-of-character question. Drop the narrative voice briefly to answer.
"Show me my character sheet" returns a structured sheet in plain text, using this format:

Character Name: [Name]
Race/Species: [Race]
Class & Level: [Class] [Level]
Background: [Background]
Alignment: [Alignment]
Experience Points: [XP]

Ability Scores:
Strength: [Score] ([Mod])
Dexterity: [Score] ([Mod])
Constitution: [Score] ([Mod])
Intelligence: [Score] ([Mod])
Wisdom: [Score] ([Mod])
Charisma: [Score] ([Mod])

Saving Throws: [List]
Skills: [List]
Passive Perception: [Value]

Combat Stats:
Armor Class: [AC]
Initiative: [Value]
Speed: [Value]
Hit Points: [HP]
Hit Dice: [Type]
Death Saves: [Status]

Attacks & Spellcasting: [Summary]

Inventory:
Equipment: [List]
Currency: [Amounts]

Spells:
[List if applicable]

Roleplaying Info:
Traits, Ideals, Bonds, Flaws
Features, Appearance, Backstory

Begin the session using only the information from the summary:`;



const newCampaignPromptHeader = `You are the Dungeon Master and Lorekeeper for the world of Alorin.

🛠️ Campaign Setup
Each campaign begins with character creation. Offer core D&D 5e options and permit custom ones.
Treat every campaign as new. Assume nothing about characters or backstories.

Ask the player to define or choose:

Starting Region

Campaign Theme

Opening Situation

World Modifier

If skipped, generate varied, lore-rooted options.
Glyphs may appear but must never dominate a campaign.


🧭 Perspective Control
Speak to the player, not about them. Never refer to the player in the third-person perspective. Always refer to the player in the second person perspective.

⚖️ Realism & Mechanics
Enforce realism. If an action defies 5e rules (e.g., flying at level 1), correct it gently and in-character.
Encourage creative risks but apply appropriate DCs and consequences.
Ensure all actions reflect level-appropriate mechanics.

🗣️ Style & Tone
Use a mature, immersive voice in the style of Brandon Sanderson—epic but grounded.
Avoid formatting symbols (e.g., ###, *, **). Write in clean, flowing prose.
Describe people, places, and objects with vivid sensory detail.
Give characters distinct, setting-appropriate voices.
Treat Alorin as a real, functioning world with logic and depth.

📘 Player Commands & OOC Triggers
"OOC:" marks an out-of-character query. Answer plainly, then resume in-world narration.
"Show me my character sheet" triggers a structured response in this format (no symbols or bullets):

Character Name: [Name]
Race/Species: [Race]
Class & Level: [Class] [Level]
Background: [Background]
Alignment: [Alignment]
Experience Points: [XP]

Ability Scores:
Strength: [Score] ([Mod])
Dexterity: [Score] ([Mod])
Constitution: [Score] ([Mod])
Intelligence: [Score] ([Mod])
Wisdom: [Score] ([Mod])
Charisma: [Score] ([Mod])

Saving Throws: [List]
Skills: [List]
Passive Perception: [Value]

Combat Stats:
Armor Class: [AC]
Initiative: [Value]
Speed: [Value]
Hit Points: [HP]
Hit Dice: [Type]
Death Saves: [Status]

Attacks & Spellcasting: [Summary]

Inventory:
Equipment: [List]
Currency: [Amounts]

Spells:
[List if applicable]

Roleplaying Info:
Traits, Ideals, Bonds, Flaws
Features, Appearance, Backstory`;


let threadID = null;
let totalTokensUsed = 0;
let hasAutosavedThisTurn = false;
let lastUserMessageTime = null;
let assistantId = null;
let narrationEnabled = false;
let selectedTTSProvider = "default";
let isMicListening = false;
let recognition = null;
let lastFinal = ""; // Stores the most recent final transcript to avoid duplicates
let sessionTokenTotal = 0;
let geminiThreadId = null;
let summaryCache = "";  // Fetched from saved file
let saveFile = {};      // Parsed SaveFile from backend

let currentSessionName = "(unnamed)";

const MAX_TOKENS_BEFORE_SUMMARY = 200000;
const geminiMemory = []; // Local runtime history
const summarizedThreads = {};
const MAX_TOKENS_PER_THREAD = 800000;



// ==========================
// === THREAD ID HELPERS ===
// ==========================


function renderMarkdownToHTML(markdown) {
  return markdown
    .replace(/</g, "&lt;").replace(/>/g, "&gt;")
    .replace(/\*\*(.*?)\*\*/g, "<strong>$1</strong>")
    .replace(/\*(.*?)\*/g, "<em>$1</em>")
    .replace(/\n/g, "<br>");
}



function getActiveThreadID() {
  return localStorage.getItem("alorinResumedThread") ||
         localStorage.getItem("alorinThread") || null;
}



function clearThreadIDs() {
  localStorage.removeItem("alorinThread");
  localStorage.removeItem("alorinResumedThread");
  threadID = null;
  updateThreadIndicator();
}


function switchTab(tabName, buttonEl) {
  const tabs = document.querySelectorAll(".tab-content");
  tabs.forEach(tab => tab.style.display = "none");

  const activeTab = document.getElementById(`tab-${tabName}`);
  if (activeTab) {
    activeTab.style.display = "block";
  }

  const allButtons = document.querySelectorAll(".tab-btn");
  allButtons.forEach(btn => btn.classList.remove("active"));
  if (buttonEl) {
    buttonEl.classList.add("active");
  }

  if (tabName === "savefile") {
    showCurrentSaveFile();
  }
}


function renderSaveFilePretty(data) {
  const s = data?.summary_cache || {};
  const pc = s.player_character || {};
  const campaign = s.campaign || {};
  const quests = campaign.active_quests || [];
  const objectives = s.ongoing_objectives || [];
  const items = pc.inventory_and_equipment || [];
  const npcs = s.key_npcs || [];
  const factions = s.factions_encountered || [];
  const notes = campaign.session_notes || [];
  const summary = campaign.summary_of_events || [];
  const world = campaign.world_state || "";
  const worldMods = campaign.world_modifiers || [];
  const location = s.current_location || "";
  const locations = s.known_locations || [];
  const situation = s.current_situation || "";
  const abilities = pc.ability_scores || {};
  const currency = pc.currency || {};
  const inventory = pc.inventory || [];
  const attacksRaw = pc.attacks_and_spellcasting;

  function section(title, contentHTML) {
    if (!contentHTML || contentHTML.trim() === "") return "";
    return `
      <div class="collapsible-section">
        <div class="collapsible-header">${title}</div>
        <div class="collapsible-content">${contentHTML}</div>
      </div>`;
  }

  let html = "";

  // Character Header
  html += `<h3>🧙 ${pc.name || "Unknown"} (${pc.character_class || "Class"} Level ${pc.level || "?"}, ${pc.race || "Race"})</h3>`;
  html += `<p><strong>Background:</strong> ${pc.background || "N/A"}<br>
  <strong>HP:</strong> ${pc.current_hp ?? "?"} / ${pc.max_hp ?? "?"} | 
  <strong>AC:</strong> ${pc.armor_class ?? "?"} | 
  <strong>Initiative:</strong> ${pc.initiative ?? "?"}</p>`;

  // Abilities
  let abilityHTML = "";
  for (const [stat, val] of Object.entries(abilities)) {
    if (typeof val === 'object' && val !== null && 'score' in val && 'mod' in val) {
      abilityHTML += `<li><strong>${stat.toUpperCase()}:</strong> ${val.score} (mod: ${val.mod >= 0 ? "+" : ""}${val.mod})</li>`;
    }
  }
  html += section("💪 Ability Scores", abilityHTML ? `<ul>${abilityHTML}</ul>` : "");

  // Inventory (separate)
  html += section("🎒 Inventory", `
    <button onclick="addInventoryItem()">➕ Add Item</button>
    <div id="inventoryInputs">
	  ${inventory.map((item, index) => `
	    <div style="margin-top: 0.5rem; display: flex; gap: 0.5rem; align-items: center;">
		  <input type="text"
			     value="${item}"
			     data-inventory-index="${index}"
			     style="flex: 1; padding: 8px; background-color: #111; color: #fff; border: 1px solid #444; border-radius: 4px;" />
		  <button onclick="removeInventoryItem(${index})" style="padding: 6px 10px; background-color: #ff4d4d; color: white; border: none; border-radius: 4px; cursor: pointer;">
		    ❌
		  </button>
	    </div>
	  `).join("")}
    </div>
  `);

  
  // Features
  let features = pc.features;
  if (typeof features === "string") {
    features = features.split(',').map(f => f.trim());
  }
  if (!Array.isArray(features)) features = [];

  html += section("🧬 Features", features.length ? `<ul>${features.map(f => `<li>${f}</li>`).join("")}</ul>` : "");
  
  
  //Skills
  let skills = pc.skills;
  if (typeof skills === "string") {
    skills = skills.split(',').map(s => s.trim());
  }
  if (!Array.isArray(skills)) skills = [];
  
  html += section("🎯 Proficiencies", skills.length ? `<ul>${skills.map(skill => `<li>${skill}</li>`).join("")}</ul>` : "");




  // Inventory & Equipment
  html += section("🧰 Inventory & Equipment", items.length ? `<ul>${items.map(i => `<li>${i}</li>`).join("")}</ul>` : "");

  // Currency (Editable)
  let currencyHTML = `
    <div id="currencyInputs" style="display: flex; flex-direction: column; gap: 0.5rem;">
      ${Object.entries(currency).map(([type, val]) => `
        <div style="display: flex; gap: 0.5rem; align-items: center;">
          <label for="currency-${type}" style="min-width: 3rem;">${type.toUpperCase()}:</label>
          <input type="number" 
                 id="currency-${type}" 
                 data-currency-type="${type}" 
                 value="${val}" 
                 style="flex: 1; padding: 8px; background-color: #111; color: #fff; border: 1px solid #444; border-radius: 4px;" />
        </div>
      `).join("")}
    </div>
  `;
  html += section("💰 Currency", currencyHTML);


  // Location & Situation
  html += section("📍 Current Location", location ? `<p>${location}</p>` : "");
  html += section("🎭 Current Situation", situation ? `<p>${situation}</p>` : "");

  // Attacks and Spellcasting (as plain text, line-split)
  const attacks = typeof attacksRaw === "string" ? attacksRaw.trim().split(/\. /) : [];
  const attackHTML = attacks.length
    ? `<ul>${attacks.map(a => `<li>${a}</li>`).join("")}</ul>`
    : "";
  html += section("⚔️ Attacks & Spellcasting", attackHTML);

  // Quests
  let questHTML = "";
  quests.forEach(q => {
    const titleLine = `
      <div class="entry-title">
        ${q.title} <em>(${q.status})</em>
      </div>`;
    const description = `<p>${q.description || ""}</p>`;
    const decisions = q.key_decisions?.length
      ? `<ul>${q.key_decisions.map(d => `<li>${d}</li>`).join("")}</ul>`
      : "";

    questHTML += `<li>${titleLine}${description}${decisions}</li>`;
  });
  html += section("📜 Active Quests", questHTML ? `<ul>${questHTML}</ul>` : "");


  // Objectives
  html += section("🎯 Ongoing Objectives", objectives.length ? `<ul>${objectives.map(o => `<li>${o}</li>`).join("")}</ul>` : "");

  // NPCs
  let npcHTML = "";
  npcs.forEach(npc => {
    const name = npc.name || "Unnamed NPC";
    const description = npc.description || "No details available";
    const r = npc.relationship || {};

    const history = r.history ? `<em>History:</em> ${r.history}<br>` : "";
    const status = r.current_status ? `<em>Status:</em> ${r.current_status}<br>` : "";
    const trust = r.trust_level != null ? `<em>Trust Level:</em> ${r.trust_level}<br>` : "";

    let notesHTML = "";
    if (Array.isArray(npc.interaction_notes) && npc.interaction_notes.length > 0) {
      notesHTML = `<details><summary>🗒️ Interaction Notes</summary><ul>${npc.interaction_notes.map(n => `<li>${n}</li>`).join("")}</ul></details>`;
    }

    npcHTML += `
      <li>
        <div class="entry-title">${name}</div>
        <p>${description}</p>
        ${history}${status}${trust}
        ${notesHTML}
      </li>`;
  });
  html += section("🤝 Key NPCs", npcHTML ? `<ul>${npcHTML}</ul>` : "");



  // Factions
  let factionHTML = "";
  factions.forEach(faction => {
    const name = faction.name || "Unknown Faction";
    const goals = faction.goals ? `<em>Goals:</em> ${faction.goals}<br>` : "";
    const summary = faction.interaction_summary ? `<em>Summary:</em> ${faction.interaction_summary}<br>` : "";
    const times = typeof faction.times_encountered === "number" ? `<em>Encounters:</em> ${faction.times_encountered}<br>` : "";
    const notes = Array.isArray(faction.interaction_notes) && faction.interaction_notes.length
      ? `<ul>${faction.interaction_notes.map(n => `<li>${n}</li>`).join("")}</ul>` : "";

    factionHTML += `<li>
      <div class="entry-title">${name}</div>
      ${goals}${summary}${times}${notes}
    </li>`;
  });
  html += section("🏰 Factions Encountered", factionHTML ? `<ul>${factionHTML}</ul>` : "");


  // Locations
  let locationHTML = "";
  locations.forEach(loc => {
    const name = loc.name || "Unnamed Location";
    const description = loc.description || "No description available.";
    const features = loc.key_features?.length
      ? `<em>Key Features:</em> <ul>${loc.key_features.map(f => `<li>${f}</li>`).join("")}</ul>`
      : "";
    const history = loc.history ? `<p><em>History:</em> ${loc.history}</p>` : "";

    locationHTML += `
      <li>
        <div class="entry-title">${name}</div>
        <p>${description}</p>
        ${features}
        ${history}
     </li>`;
  });

html += section("🗺️ Known Locations", locationHTML ? `<ul>${locationHTML}</ul>` : "");



  // Session Notes
  html += section("🧾 Session Notes", notes.length ? `<ul>${notes.map(n => `<li>${n}</li>`).join("")}</ul>` : "");

  // Summary
  html += section("📖 Summary of Events", summary.length ? summary.map(ev => `<p>${ev}</p>`).join("") : "");

  // World
  html += section("🌍 World State", world ? `<p>${world}</p>` : "");
  html += section("🌐 World Modifiers", worldMods.length ? `<ul>${worldMods.map(wm => `<li>${wm}</li>`).join("")}</ul>` : "");
  
  html += `
  <div style="margin-top: 2rem;">
    <button onclick="submitSaveFile()" style="padding: 10px 16px; font-weight: bold; background: #66fcf1; color: #0b0c10; border: none; border-radius: 6px; cursor: pointer;">
      💾 Save Changes
    </button>
  </div>
`;


  return html;
}








function storeGeminiTurn(role, content) {
  geminiMemory.push({ role, content });

  // Optional: cap local memory at 100 turns
  if (geminiMemory.length > 100) {
    geminiMemory.shift();
  }
}

function getLastGeminiTurns(n = 3) {
  return geminiMemory.slice(-n * 2) // 3 exchanges = 6 messages
    .map(m => `${m.role === "user" ? "Player" : "DM"}: ${m.content}`)
    .join("\n\n");
}


function appendToChatLog(role, text) {
  const chatLog = document.getElementById("chatLog");

  const wrapper = document.createElement("div");
  wrapper.className = role === "user" ? "chat-bubble user-bubble" : "chat-bubble assistant-bubble";

  const label = document.createElement("div");
  label.className = "chat-label";
  label.textContent = role === "user" ? "You:" : "Narrator:";

  const content = document.createElement("div");
  content.className = "chat-content";
  content.textContent = text;

  wrapper.appendChild(label);
  wrapper.appendChild(content);
  chatLog.appendChild(wrapper);

  chatLog.scrollTop = chatLog.scrollHeight;
}



function showLoading(message = "⏳ Working... please wait") {
  const overlay = document.getElementById("loadingOverlay");
  overlay.textContent = message;
  overlay.style.display = "block";
}

function hideLoading() {
  const overlay = document.getElementById("loadingOverlay");
  overlay.style.display = "none";
}


// =======================
// === TOKEN ESTIMATES ===
// =======================


function updateTokenBar(percent) {
  const bar = document.getElementById("tokenBar");
  const label = document.getElementById("tokenPercent");
  if (!bar || !label) return;

  bar.style.width = `${percent}%`;
  label.textContent = `${percent}%`;

  if (percent < 70) {
    bar.style.backgroundColor = "#66fcf1";
  } else if (percent < 90) {
    bar.style.backgroundColor = "#ffc107";
  } else {
    bar.style.backgroundColor = "#ff4d4d";
  }
}


function displayTokenStats(usage) {
  if (!usage) return;

  // Normalize key names (whether from OpenAI or backend)
  const prompt = usage.prompt_tokens ?? usage.prompt ?? 0;
  const completion = usage.completion_tokens ?? usage.completion ?? 0;
  const total = usage.total_tokens ?? usage.total ?? 0;

  document.getElementById("tokenPrompt").textContent = prompt;
  document.getElementById("tokenCompletion").textContent = completion;
  document.getElementById("tokenTotal").textContent = total;
}






function cleanSaveFile(obj) {
  // Deep clone to avoid mutating the original
  const clone = JSON.parse(JSON.stringify(obj));

  // Ensure session ID and timestamp are strings
  clone.session_id = String(clone.session_id || crypto.randomUUID());
  clone.timestamp = new Date().toISOString();

  // Validate and clean player_character
  if (clone.player_character) {
    const pc = clone.player_character;
    pc.name = String(pc.name || "Unknown");
    pc.character_class = String(pc.character_class || "Unknown");
    pc.race = String(pc.race || "Unknown");
    pc.background = String(pc.background || "Unknown");
    pc.level = parseInt(pc.level) || 1;
    pc.max_hp = parseInt(pc.max_hp) || 10;
    pc.current_hp = parseInt(pc.current_hp) || pc.max_hp;
    pc.inventory = Array.isArray(pc.inventory) ? pc.inventory : [];
    pc.notable_traits = String(pc.notable_traits || "");
    pc.spell_slots = pc.spell_slots || {};
  }

  // Validate key_npcs array
  if (!Array.isArray(clone.key_npcs)) clone.key_npcs = [];

  // Validate factions array
  if (!Array.isArray(clone.factions_encountered)) clone.factions_encountered = [];

  // Validate campaign object
  if (!clone.campaign) clone.campaign = {
    summary_of_events: [],
    world_state: "",
    ongoing_objectives: [],
    inventory_and_equipment: [],
    campaign_variables: "",
    current_location: "",
    current_situation: ""
  };

  return clone;
}

// ============================
// === MARKDOWN -> HTML UTILS ===
// ============================



function cleanHint(input) {
  const patterns = [
    /^who is\s+/i, /^what is\s+/i, /^tell me about\s+/i, /^describe\s+/i,
    /^where is\s+/i, /^do you know\s+/i, /^is there a\s+/i, /^\s*the\s+/i
  ];
  let cleaned = input.toLowerCase().trim();
  for (const p of patterns) cleaned = cleaned.replace(p, "");
  return cleaned.replace(/[?.!,;:]+$/, "").trim();
}

// ==========================
// === ASSISTANT LOGIC ====
// ==========================


async function waitForSummaryUpdate(threadId, previousTokenMark, baseDelay = 500, jitter = 250, maxDelay = 15000) {
  let attempt = 0;

  while (true) {
    try {
      const res = await fetch(`/api/data/${threadId}.json`, {
							headers: {
								"x-api-key": "qaSWEDCFRewsa-OIJH_iuyhgTRFDSDyhgFRdeDFR"
							}
	  });
      if (res.ok) {
        const json = await res.json();
        const current = json?.last_summarized_token_usage || 0;

        if (current > previousTokenMark) {
          console.log(`✅ Summary token usage updated: ${previousTokenMark} → ${current}`);
          return true;
        } else {
          console.log(`🕒 Summary token usage not updated yet: still ${current}`);
        }
      }
    } catch (err) {
      console.warn("⚠️ Could not fetch thread data for summary check:", err);
    }

    const exponential = baseDelay * (2 ** attempt);
    const delay = Math.min(exponential + Math.random() * jitter, maxDelay);

    console.warn(`🔁 Waiting ${Math.round(delay)}ms for summary update (attempt ${attempt + 1})...`);
    await new Promise((resolve) => setTimeout(resolve, delay));

    attempt++;
  }
}


async function showCurrentSaveFile() {
  const threadId = geminiThreadId;
  if (!threadId) {
    document.getElementById("saveFileDisplay").innerHTML = "<p>No active thread.</p>";
    return;
  }

  try {
    const res = await fetch(`/api/save/${threadId}`, {
      headers: { "x-api-key": "qaSWEDCFRewsa-OIJH_iuyhgTRFDSDyhgFRdeDFR" },
    });

    if (!res.ok) throw new Error("Save file not found.");

    const json = await res.json();
    console.log("🔍 Save File Loaded:", json);

    saveFile = json;  // ✅ This is the critical missing step

    const prettyHTML = renderSaveFilePretty(json);
    document.getElementById("saveFileDisplay").innerHTML = prettyHTML;

  } catch (err) {
    console.error("❌ Failed to load save file:", err);
    document.getElementById("saveFileDisplay").innerHTML =
      `<p style="color: red;">⚠️ Failed to load save file.<br>${err.message}</p>`;
  }
}


async function submitSaveFile() {
  syncInventoryInputsToSaveFile(); // Ensure in-memory state is current
  syncCurrencyInputsToSaveFile(); // Ensure in-memory state is current

  const payload = {
    inventory: saveFile.summary_cache?.player_character?.inventory,
    currency: saveFile.summary_cache?.player_character?.currency,
  };

  const res = await fetch(`/api/save/${saveFile.thread_id}`, {
    method: "PATCH",
    headers: {
      "Content-Type": "application/json",
      "x-api-key": "qaSWEDCFRewsa-OIJH_iuyhgTRFDSDyhgFRdeDFR",
    },
    body: JSON.stringify(payload),
  });

  if (!res.ok) {
    const err = await res.json();
    console.error("❌ Save failed:", err);
    alert("Save failed: " + err.detail);
    return;
  }

  showToast("✅ Inventory updated successfully.");
}



function removeInventoryItem(index) {
  const container = document.querySelector(`#inventoryInputs div:nth-child(${index + 1})`);
  if (container) container.remove();

  // Optional: sync immediately so blank doesn't linger
  syncInventoryInputsToSaveFile();
}





function syncInventoryInputsToSaveFile() {
  const inputs = document.querySelectorAll('#inventoryInputs input[data-inventory-index]');
  const newInventory = [];

  inputs.forEach(input => {
    const value = input.value.trim();
    if (value !== "") {
      newInventory.push(value);
    }
  });

  if (
    saveFile?.summary_cache?.player_character &&
    Array.isArray(newInventory)
  ) {
    saveFile.summary_cache.player_character.inventory = newInventory;
  }
}


function syncCurrencyInputsToSaveFile() {
  if (!saveFile?.summary_cache?.player_character?.currency) {
    console.warn("No currency section in saveFile");
    return;
  }

  const inputs = document.querySelectorAll('[data-currency-type]');
  inputs.forEach(input => {
    const type = input.getAttribute('data-currency-type');
    const val = parseInt(input.value, 10);
    saveFile.summary_cache.player_character.currency[type] = isNaN(val) ? 0 : val;
  });
}



function addInventoryItem() {
  const inventoryInputs = document.getElementById("inventoryInputs");
  if (!inventoryInputs) return;

  const index = inventoryInputs.children.length;

  // Create container
  const div = document.createElement("div");
  div.style.marginTop = "0.5rem";
  div.style.display = "flex";
  div.style.gap = "0.5rem";
  div.style.alignItems = "center";

  // Create input
  const input = document.createElement("input");
  input.type = "text";
  input.placeholder = "New item...";
  input.setAttribute("data-inventory-index", index);
  input.style.flex = "1";
  input.style.padding = "8px";
  input.style.backgroundColor = "#111";
  input.style.color = "#fff";
  input.style.border = "1px solid #444";
  input.style.borderRadius = "4px";

  // Create remove button
  const removeBtn = document.createElement("button");
  removeBtn.textContent = "❌";
  removeBtn.style.padding = "6px 10px";
  removeBtn.style.backgroundColor = "#ff4d4d";
  removeBtn.style.color = "white";
  removeBtn.style.border = "none";
  removeBtn.style.borderRadius = "4px";
  removeBtn.style.cursor = "pointer";
  removeBtn.onclick = () => {
    div.remove();
    syncInventoryInputsToSaveFile(); // update after removal
  };

  // Attach input & button
  div.appendChild(input);
  div.appendChild(removeBtn);
  inventoryInputs.appendChild(div);
}



async function preloadGeminiMemory(threadId) {
  try {
    const res = await fetch(`/api/gemini/thread/${threadId}`, {
						headers: {
							"x-api-key": "qaSWEDCFRewsa-OIJH_iuyhgTRFDSDyhgFRdeDFR"
						}
	});
    const messages = await res.json();

    geminiMemory.length = 0; // Clear any previous memory

    for (const { role, content } of messages) {
      storeGeminiTurn(role, content);
    }

    console.log(`✅ Rehydrated ${geminiMemory.length} Gemini messages`);

  } catch (err) {
    console.error("❌ Failed to load Gemini memory from server:", err);
  }
}




async function checkIfAutoSummaryNeeded(threadId) {
  if (!threadId) {
    console.warn("⚠️ No thread ID provided for auto-summary check");
    return;
  }

  let lastSummarized = 0;
  try {
    const res = await fetch(`/api/data/${threadId}.json`, {
      headers: { "x-api-key": "qaSWEDCFRewsa-OIJH_iuyhgTRFDSDyhgFRdeDFR" }
    });
    const json = await res.json();
    lastSummarized = json.last_summarized_token_usage || 0;
  } catch (err) {
    console.warn("⚠️ Failed to fetch last summary snapshot", err);
  }

  const tokenDelta = sessionTokenTotal - lastSummarized;
  const canAct = tokenDelta >= MAX_TOKENS_BEFORE_SUMMARY;
  const mustRollover = sessionTokenTotal >= MAX_TOKENS_PER_THREAD;

  console.log(`[DEBUG] Token summary check for thread ${threadId}`);
  if (!canAct) return;

  if (mustRollover) {
    console.log("🔄 Gemini thread rollover triggered...");
    await rolloverGeminiThread();
  } else {
    console.log("🧠 Triggering auto-summary for thread:", threadId);
    const summaryOK = await autoSummarizeGeminiThread(threadId);
    if (summaryOK) {
      await loadGeminiSessionState(threadId);
      lastSummaryTurnCount = 0;
    }
  }
}





async function rolloverGeminiThread() {
  showLoading("🔄 Starting new chapter...");

  try {
    const oldThreadId = geminiThreadId;

    const sessionName = await promptGeminiSession();
    if (!sessionName) {
      alert("A session name is required.");
      throw new Error("Session name missing");
    }

    let previousTokenMark = 0;
    try {
      const dataRes = await fetch(`/api/data/${oldThreadId}.json`, {
								headers: {
									"x-api-key": "qaSWEDCFRewsa-OIJH_iuyhgTRFDSDyhgFRdeDFR"
								}
	  });
      const dataJson = await dataRes.json();
      previousTokenMark = dataJson.last_summarized_token_usage || 0;
    } catch (err) {
      console.warn("⚠️ Could not fetch previous token mark — assuming 0", err);
    }

    // ⬅️ Trigger summary but let us wait manually
    const summaryStarted = await autoSummarizeGeminiThread(oldThreadId, {
      waitForCompletion: false,
      previousTokenMark: previousTokenMark
    });

    if (!summaryStarted) throw new Error("Auto-summary did not start");

    await waitForSummaryUpdate(oldThreadId, previousTokenMark);

    const saveRes = await fetch(`/api/save/${oldThreadId}`, {
							headers: {
								"x-api-key": "qaSWEDCFRewsa-OIJH_iuyhgTRFDSDyhgFRdeDFR"
							}
	});
    const saveData = await saveRes.json();
    const summaryCache = saveData.summary_cache;

    if (!summaryCache || typeof summaryCache !== "object" || !summaryCache.player_character) {
      throw new Error("❌ Summary file missing or invalid.");
    }

    const res = await fetch("/api/gemini/session", {
      method: "POST",
      headers: { "Content-Type": "application/json",
				 "x-api-key": "qaSWEDCFRewsa-OIJH_iuyhgTRFDSDyhgFRdeDFR"
	  },
      body: JSON.stringify({ session_name: sessionName }),
    });

    const threadData = await res.json();
    const newThreadId = threadData.thread_id;
    if (!newThreadId) throw new Error("❌ No thread ID returned.");

    const kickoffRes = await fetch("/api/gemini/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json",
				 "x-api-key": "qaSWEDCFRewsa-OIJH_iuyhgTRFDSDyhgFRdeDFR"
	  },
      body: JSON.stringify({
        prompt: "[continuing…]",
        thread_id: newThreadId,
        system_instruction: staticInstructions,
        bootstrap_memory: summaryCache
      }),
    });

    const kickoffData = await kickoffRes.json();
    const replyText = kickoffData.response || "[No response from Gemini]";

    geminiThreadId = newThreadId;

    const dmEntry = document.createElement("div");
    dmEntry.className = "chat-entry dm";
    dmEntry.innerHTML = `<pre><strong>📜 DM (Gemini):</strong>\n${replyText.trim()}</pre><hr>`;
    chatLog.appendChild(dmEntry);
    chatLog.scrollTop = chatLog.scrollHeight;

    await loadGeminiSessionState(newThreadId);
    sessionTokenTotal = 0;
    lastSummaryTurnCount = 0;
	
	try {
		await fetch("/api/merge_saves", {
			method: "POST",
			headers: {
				"Content-Type": "application/json",
				"x-api-key": "qaSWEDCFRewsa-OIJH_iuyhgTRFDSDyhgFRdeDFR"
			},
			body: JSON.stringify({ old_id: oldThreadId, new_id: newThreadId })
		});
	} catch (mergeErr) {
		console.warn("⚠️ Save merge failed:", mergeErr);
	}


    showToast("✅ New chapter started");

  } catch (err) {
    console.error("❌ Gemini thread rollover failed:", err);
    showToast("⚠️ Could not start a new session");
  } finally {
    hideLoading(); // ✅ Always hide overlay once we’re done
  }
}




async function autoSummarizeGeminiThread(threadId, options = {}) {
  const { waitForCompletion = true, previousTokenMark = null } = options;

  try {
    showLoading("📘 Generating SaveFile and Summary...");

    let tokenMark = previousTokenMark;

    if (tokenMark === null) {
      try {
        const dataRes = await fetch(`/api/data/${threadId}.json`, {
								headers: {
									"x-api-key": "qaSWEDCFRewsa-OIJH_iuyhgTRFDSDyhgFRdeDFR"
								}
		});
        const dataJson = await dataRes.json();
        tokenMark = dataJson.last_summarized_token_usage || 0;
      } catch (err) {
        console.warn("⚠️ Could not fetch previous token mark — assuming 0", err);
        tokenMark = 0;
      }
    }

    const res = await fetch("/api/save/summarize-gemini", {
      method: "POST",
      headers: { "Content-Type": "application/json",
				 "x-api-key": "qaSWEDCFRewsa-OIJH_iuyhgTRFDSDyhgFRdeDFR"
	  },
      body: JSON.stringify({ thread_id: threadId }),
    });

    if (!res.ok) {
      const errText = await res.text();
      console.warn("❌ Summary request failed:", errText);
      showToast("⚠️ Auto-summary failed to start");
      return false;
    }

    showToast("🧠 Summary queued. Waiting for backend to finish...");

    if (waitForCompletion) {
      await waitForSummaryUpdate(threadId, tokenMark);
      await loadGeminiSessionState(threadId);
      showToast("✅ Summary and SaveFile complete");
	  hideLoading();
    }

    return true;

  } catch (err) {
    console.error("❌ Auto-summary failed:", err);
    showToast("⚠️ Auto-summary failed");
    hideLoading(); // Ensure overlay disappears on error
    return false;
  }
}








async function loadGeminiSessionState(threadId) {
  let saveExists = false;

  try {
    const res = await fetch(`/api/save/${threadId}`, {
						headers: {
							"x-api-key": "qaSWEDCFRewsa-OIJH_iuyhgTRFDSDyhgFRdeDFR"
						}
	});
    if (res.ok) {
      const parsedSave = await res.json();
      saveFile = parsedSave;
      summaryCache = parsedSave.summary_cache || "(no summary)";
      summarizedThreads[threadId] = true;  // ✅ Mark this specific thread as summarized
      saveExists = true;
      console.log("✅ Save memory loaded into frontend context");
    } else if (res.status !== 404) {
      console.warn(`⚠️ Failed to load save file: HTTP ${res.status}`);
    } else {
      saveFile = null;
      summaryCache = null;
    }
  } catch (err) {
    console.error("❌ Unexpected error while fetching save file:", err);
    saveFile = null;
    summaryCache = null;
  }

  await loadGeminiTokenStatsFromData(threadId);
  return saveExists;
}







// Fetch accurate token total from backend
async function loadGeminiTokenStatsFromData(threadId) {
  try {
    const res = await fetch(`/api/data/${threadId}.json`, {
								headers: {
									"x-api-key": "qaSWEDCFRewsa-OIJH_iuyhgTRFDSDyhgFRdeDFR"
								}
	});
    if (!res.ok) {
      if (res.status === 404) {
        console.warn(`⚠️ No /data file found yet for thread ${threadId}`);
        return;
      }
      throw new Error(`Unexpected HTTP error: ${res.status}`);
    }

    const data = await res.json();
    const total = data.token_usage || 0;
    const lastSummary = data.last_summarized_token_usage || 0;
    const delta = total - lastSummary;

    sessionTokenTotal = total;

    const html = `
      📏 Total Gemini Tokens Used: ${total.toLocaleString()}<br>
      🔄 Tokens Since Last Summary: ${delta.toLocaleString()}
    `;

    const tokenDiv = document.getElementById("sessionTokens");
    if (tokenDiv) tokenDiv.innerHTML = html;

    console.log("✅ Token stats loaded from /data/");
  } catch (err) {
    console.error("❌ Failed to load token stats from /data/:", err);
  }
}

// ================================
// === POLL RUN STATUS (General) ===
// ================================

async function pollRunStatus(threadId, runId) {
  let totalTokensFromRun = 0;

  // Fetch token usage from Gemini /data endpoint
  for (let i = 0; i < 60; i++) {
    try {
      const res = await fetch(`/api/data/${threadId}.json`, {
		  headers: {
			  "x-api-key": "qaSWEDCFRewsa-OIJH_iuyhgTRFDSDyhgFRdeDFR"
		  }
	  });
      const data = await res.json();
      const usage = {
        prompt_tokens: 0,
        completion_tokens: 0,
        total_tokens: data.token_usage || 0
      };

      totalTokensFromRun = usage.total_tokens;

      const currentPrompt = parseInt(document.getElementById("tokenPrompt").textContent) || 0;
      const currentCompletion = parseInt(document.getElementById("tokenCompletion").textContent) || 0;
      const currentTotal = parseInt(document.getElementById("tokenTotal").textContent) || 0;

      const newTotal = usage.total_tokens;
      const newPrompt = currentPrompt;      // Gemini doesn't differentiate
      const newCompletion = currentCompletion;

      displayTokenStats({
        prompt_tokens: newPrompt,
        completion_tokens: newCompletion,
        total_tokens: newTotal
      });

      const percent = Math.floor((newTotal / 128000) * 100);
      updateTokenBar(percent);

      const total = data.token_usage || 0;
      const lastSummary = data.last_summarized_token_usage || 0;
      const delta = total - lastSummary;

      document.getElementById("sessionTokens").innerHTML = `
        📏 Total Gemini Tokens Used: ${total.toLocaleString()}<br>
        🔄 Tokens Since Last Summary: ${delta.toLocaleString()}
      `;


      // Exit early since Gemini doesn't need repeated polling
      break;

    } catch (err) {
      console.warn("⚠️ Could not update token delta from /data/", err);
    }

    await new Promise(r => setTimeout(r, 2000));
  }

  return true;
}









// ===================================
// === HANDLE TOOL CALLS FROM GPT ===
// ===================================





// ==========================
// === DOM ELEMENTS & UI ===
// ==========================

// DOM access
const inputBox = document.getElementById("userInput");
const modelSelect = document.getElementById("modelSelect");
const ttsSelect = document.getElementById("ttsSelect");
const narrateCheckbox = document.getElementById("narrateToggle");
const googleVoiceContainer = document.getElementById("googleVoiceContainer");
const googleVoiceSelect = document.getElementById("googleVoiceSelect");
const googleVoiceTooltip = document.getElementById("googleVoiceTooltip");
const tokenBar = document.getElementById("tokenBar");
const tokenPercent = document.getElementById("tokenPercent");

// Google TTS voice labels
const voiceDescriptions = {
  "en-US-Standard-C": "Calm and neutral male voice ($)",
  "en-US-Standard-D": "Strong, authoritative male tone ($)",
  "en-US-Standard-E": "Gentle, expressive female voice ($)",
  "en-US-Wavenet-D": "Natural and premium male voice ($$)",
  "en-US-Wavenet-F": "Warm and lifelike female voice ($$)",
  "en-US-Polyglot-1": "Quasi high quality male voice ($$)",
  "en-US-Chirp3-HD-Achernar": "Chirp3 HD – Achernar (Warm Female) ($$$)",
  "en-US-Chirp3-HD-Iapetus": "Chirp3 HD – Iapetus (Deep Male) ($$$)"
};

// Voice dropdown tooltip binding
ttsSelect.addEventListener("change", () => {
  const selectedTTS = ttsSelect.value;
  googleVoiceContainer.style.display = selectedTTS === "google" ? "block" : "none";
});
ttsSelect.dispatchEvent(new Event("change"));

googleVoiceSelect.addEventListener("change", () => {
  const selected = googleVoiceSelect.value;
  googleVoiceTooltip.textContent = voiceDescriptions[selected] || "";
});
googleVoiceSelect.dispatchEvent(new Event("change"));

// Enter-to-send binding
inputBox.addEventListener("keydown", (event) => {
  if (event.key === "Enter" && !event.shiftKey) {
    event.preventDefault();
    sendToGPT(); // This function is defined in Part 4
  }
});

// Display narration manually in chat
function displayNarration(text) {
  const message = document.createElement("div");
  message.className = "assistant";
  message.textContent = text;
  chatLog.appendChild(message);
  chatLog.scrollTop = chatLog.scrollHeight;
}


function showToast(message, duration = 4000) {
  const toast = document.createElement("div");
  toast.className = "toast-message";
  toast.textContent = message;
  document.body.appendChild(toast);

  setTimeout(() => {
    toast.classList.add("fade-out");
    toast.addEventListener("transitionend", () => toast.remove());
  }, duration);
}



// Voice input binding
document.getElementById("voiceBtn")?.addEventListener("click", () => {
  if (!("webkitSpeechRecognition" in window)) {
    alert("Speech Recognition not supported in this browser.");
    return;
  }

  // Only initialize once
  if (!recognition) {
    recognition = new webkitSpeechRecognition();
    recognition.continuous = true;
    recognition.interimResults = true;
    recognition.lang = "en-US";

    let lastFinal = "";

    recognition.onresult = (event) => {
      let finalTranscript = "";

      for (let i = event.resultIndex; i < event.results.length; ++i) {
        if (event.results[i].isFinal) {
          finalTranscript += event.results[i][0].transcript;
        }
      }

      finalTranscript = finalTranscript.trim();

      if (!finalTranscript) return;

      if (!lastFinal) {
        // First run: use full transcript
        inputBox.value += (inputBox.value ? " " : "") + finalTranscript;
        lastFinal = finalTranscript;
        return;
      }

      if (finalTranscript !== lastFinal) {
        const newText = finalTranscript.replace(lastFinal, "").trim();
        if (newText) {
          inputBox.value += (inputBox.value ? " " : "") + newText;
        }
        lastFinal = finalTranscript;
      }
    };

    recognition.onerror = (e) => {
      console.error("🎤 Speech recognition error:", e);
    };

    recognition.onend = () => {
      if (isMicListening) {
        recognition.start(); // Auto-restart if toggled on
      }
    };
  }

  // Toggle microphone on/off
  if (isMicListening) {
    recognition.stop();
    isMicListening = false;
    document.getElementById("voiceBtn").innerText = "🎙️";
  } else {
    recognition.start();
    isMicListening = true;
    document.getElementById("voiceBtn").innerText = "🔴";
  }
});


async function waitForFilesUntilAvailable(threadId, baseDelay = 500, jitter = 250, maxDelay = 15000) {
  let attempt = 0;

  while (true) {
    const [saveRes, dataRes] = await Promise.all([
      fetch(`/api/save/${threadId}`),
      fetch(`/api/data/${threadId}.json`)
    ]);

    const saveReady = saveRes.ok;
    const dataReady = dataRes.ok;

    if (saveReady && dataReady) {
      console.log("✅ Both save and data files are now available");
      return true;
    }

    const exponential = baseDelay * (2 ** attempt);
    const delay = Math.min(exponential + Math.random() * jitter, maxDelay);

    console.warn(`🔁 Waiting ${Math.round(delay)}ms for save/data files (attempt ${attempt + 1})...`);
    await new Promise(resolve => setTimeout(resolve, delay));

    attempt++;
  }
}




async function sendToGPT() {
  const input = inputBox.value.trim();
  if (!input) return;

  const selectedModel = document.getElementById("modelSelect")?.value || "gpt-4o";

  // 💬 Show user message
  const userEntry = document.createElement("div");
  userEntry.className = "chat-entry user";
  userEntry.innerHTML = `<pre><strong>🧝 You:</strong>\n${input}</pre>`;
  chatLog.appendChild(userEntry);

  const loadingDiv = document.createElement("div");
  loadingDiv.className = "chat-entry loading";
  loadingDiv.innerText = "📜 Weaving your tale...";
  chatLog.appendChild(loadingDiv);
  chatLog.scrollTop = chatLog.scrollHeight;

  try {
    // === GEMINI PATH ===
	if (selectedModel === "gemini") {
	  const systemInstruction = staticInstructions;

	  // 🛡 Ensure thread ID exists before using it
	  if (!geminiThreadId) {
		console.warn("⚠️ No thread — prompting for new Gemini session");
		await rolloverGeminiThread();

		if (!geminiThreadId) {
		  console.error("❌ Still no thread after prompt — aborting");
		  return;
		}
	  }

	  // 🔄 Load the latest save + token data
	  await loadGeminiSessionState(geminiThreadId);


	  const promptPayload = input;  // just the player's message


	  const res = await fetch("/api/gemini/chat", {
		method: "POST",
		headers: { 
			"Content-Type": "application/json",
			"x-api-key": "qaSWEDCFRewsa-OIJH_iuyhgTRFDSDyhgFRdeDFR"
		},
		body: JSON.stringify({
		  prompt: promptPayload,
		  thread_id: geminiThreadId,
		  system_instruction: systemInstruction
		})
	  });

	  const data = await res.json();
	  const newThreadId = data.thread_id;
	  geminiThreadId = newThreadId;

	  const replyText = data.response || "[No response from Gemini]";

	  // 💬 Add Gemini reply to chat
	  const dmEntry = document.createElement("div");
	  dmEntry.className = "chat-entry dm";
	  dmEntry.innerHTML = `<pre><strong>📜 DM (Gemini):</strong>\n${replyText.trim()}</pre><hr>`;
	  chatLog.appendChild(dmEntry);

	  // 🔄 Refresh memory and stats after reply
	  await loadGeminiSessionState(newThreadId);

	  // 🧠 Local runtime state
	  inputBox.value = "";
	  loadingDiv.remove();
	  chatLog.scrollTop = chatLog.scrollHeight;

	  storeGeminiTurn("user", input);
	  storeGeminiTurn("gemini", replyText);

	  // ✅ Now uses updated thread ID safely
	  await checkIfAutoSummaryNeeded(newThreadId);
	  return;
	}


  } catch (err) {
    console.error("❌ Error in sendToGPT:", err);
    loadingDiv.remove();
    alert("An error occurred while sending your message.");
  }
}







async function narrateAsync(text, ttsProvider) {
  try {
    if (!text || !ttsProvider) {
      console.warn("🔇 Narration skipped: Missing text or provider.");
      return;
    }

    let voice = null;

    if (ttsProvider === "google") {
      const voiceDropdown = document.getElementById("googleVoiceSelect");
      voice = voiceDropdown?.value || "en-US-Wavenet-D";
    } else if (ttsProvider === "openai") {
      voice = "shimmer"; // OpenAI supported voices: shimmer, echo, fable, onyx, nova, alloy
    } else if (ttsProvider === "browser") {
      const utterance = new SpeechSynthesisUtterance(text);
      speechSynthesis.speak(utterance);
      return;
    } else {
      console.warn(`🔇 Unknown TTS provider: ${ttsProvider}`);
      return;
    }

    const response = await fetch("/api/tts", {
      method: "POST",
      headers: { "Content-Type": "application/json",
			     "x-api-key": "qaSWEDCFRewsa-OIJH_iuyhgTRFDSDyhgFRdeDFR"
	  },
      body: JSON.stringify({ text, provider: ttsProvider, voice })
    });

    if (!response.ok) {
      const errorDetails = await response.text();
      throw new Error(`Narration failed: ${errorDetails}`);
    }

    const audioData = await response.arrayBuffer();
    const blob = new Blob([audioData], { type: "audio/mpeg" });
    const audioUrl = URL.createObjectURL(blob);
    const audio = new Audio(audioUrl);
    audio.play();

  } catch (err) {
    console.error("🎧 Narration error:", err);
    alert("Narration failed. Check the console for more details.");
  }
}

async function sendGeminiCampaignKickoff() {
  try {
    showLoading("📖 Launching campaign...");

    const res = await fetch("/api/gemini/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json",
				 "x-api-key": "qaSWEDCFRewsa-OIJH_iuyhgTRFDSDyhgFRdeDFR"
	  },
      body: JSON.stringify({
        prompt: newCampaignPromptHeader,
        thread_id: geminiThreadId || null,
        system_instruction: staticInstructions  // or newCampaignPromptHeader if appropriate
      })
    });

    const data = await res.json();
    geminiThreadId = data.thread_id;

    const replyText = data.response || "[No response from Gemini]";

    const dmEntry = document.createElement("div");
    dmEntry.className = "chat-entry dm";
    dmEntry.innerHTML = `<pre><strong>📜 DM (Gemini):</strong>\n${replyText.trim()}</pre><hr>`;
    chatLog.appendChild(dmEntry);
    chatLog.scrollTop = chatLog.scrollHeight;

    hideLoading();
  } catch (err) {
    console.error("❌ Error sending kickoff:", err);
    hideLoading();
    alert("Failed to start the campaign.");
  }
}



async function promptGeminiSession() {
  try {
    const res = await fetch("/api/gemini/sessions", {
		headers: {
			"x-api-key": "qaSWEDCFRewsa-OIJH_iuyhgTRFDSDyhgFRdeDFR"
		}
	});
    if (!res.ok) throw new Error("Failed to fetch sessions");

    const sessions = await res.json();
    let promptMessage = "🧙 Available Gemini sessions:\n\n";

    if (sessions.length > 0) {
      promptMessage += sessions.map(s => `• ${s}`).join("\n");
      promptMessage += "\n\nEnter a session name to load or create:";
    } else {
      promptMessage = "🧙 No saved sessions found.\nEnter a session name to begin:";
    }

    const sessionName = prompt(promptMessage);
    return sessionName?.trim();
  } catch (err) {
    console.error("❌ Could not load Gemini session list:", err);
    return prompt("Enter a session name to continue or start:");
  }
}




document.addEventListener("DOMContentLoaded", async () => {
  console.log("✅ DOM fully loaded");
  

const sessionName = await promptGeminiSession();
if (!sessionName) {
  alert("A session name is required.");
  throw new Error("Session name missing");
}

if (geminiThreadId) {
  await preloadGeminiMemory(geminiThreadId);
}


// 🧠 Ask backend for thread ID
const threadRes = await fetch("/api/gemini/session", {
  method: "POST",
  headers: { "Content-Type": "application/json",
			 "x-api-key": "qaSWEDCFRewsa-OIJH_iuyhgTRFDSDyhgFRdeDFR"
		   },
  body: JSON.stringify({ session_name: sessionName })
});
const threadData = await threadRes.json();
geminiThreadId = threadData.thread_id;

// 🧠 Load chat history
const historyRes = await fetch(`/api/gemini/thread/${geminiThreadId}`, {
							headers: {
								"x-api-key": "qaSWEDCFRewsa-OIJH_iuyhgTRFDSDyhgFRdeDFR"
							}
});
const historyData = await historyRes.json();
const messages = historyData.messages || [];

for (const msg of messages) {
  const entry = document.createElement("div");
  entry.className = "chat-entry " + (msg.role === "user" ? "user" : "dm");

  const prefix = msg.role === "user" ? "🧝 You" : "📜 DM (Gemini)";
  entry.innerHTML = `<pre><strong>${prefix}:</strong>\n${msg.content.trim()}</pre>`;
  chatLog.appendChild(entry);
}
chatLog.scrollTop = chatLog.scrollHeight;


document.addEventListener("click", function (e) {
  if (e.target.classList.contains("collapsible-header")) {
    const section = e.target.parentElement;
    section.classList.toggle("active");
  }
});



document.getElementById("startGEMBtn").addEventListener("click", () => {
  sendGeminiCampaignKickoff();
});
  
  
  // === Model description helper ===
const modelDescriptions = {
  "gpt-3.5-turbo": "💸 Fast & cheap. Good for quick narration and basic queries.",
  "gpt-4o-mini": "⚖️ Balanced. Great for solid performance at a lower cost.",
  "gpt-4o": "🧠 Highest quality. Best for emotional depth and immersive storytelling."
};

function updateModelInfo() {
  const model = document.getElementById("modelSelect")?.value || "gpt-4o";
  const infoBox = document.getElementById("modelInfo");
  if (infoBox) {
    infoBox.textContent = modelDescriptions[model] || "Model description unavailable.";
  }
}

document.getElementById("modelSelect")?.addEventListener("change", updateModelInfo);
updateModelInfo(); // Set initial state


console.log("✅ DOM ready and UI initialized.");

});