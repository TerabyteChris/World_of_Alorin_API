from fastapi import FastAPI, HTTPException
from typing import List, Dict

app = FastAPI(title="World of Alorin API", version="1.0")

# === VESTALS ===
vestals = {
    # Full Vestal definitions from previous messages...
}

@app.get("/vestals", response_model=List[str])
def list_vestals():
    return list(vestals.keys())

@app.get("/vestals/{name}")
def get_vestal(name: str):
    if name not in vestals:
        raise HTTPException(status_code=404, detail="Vestal not found")
    return vestals[name]

# === NPCs ===
npcs = {
    "Sergeth the Gray": {
        "name": "Sergeth the Gray",
        "title": "Glyph Theorist in Residence",
        "race": "Half-Elf (or possibly altered human)",
        "age": "Estimated mid-50s (biological), though his vitality appears unnaturally preserved",
        "pronouns": "He/Him",
        "alignment": "Neutral",
        "affiliation": "The Order (Grayhand Operative)",
        "aliases": ["The Gray Archivist", "Whisper of Lost Threads", "Fieldwalker of Quiet Tomes"],
        "public_role": "Glyph Theorist in Residence – 3rd Strand Temple Archives (Unofficial)",
        "background": "Once a scribe for the Sigil Covenant, Sergeth vanished from Agasan records three decades ago. Though presumed dead, he resurfaced under many names in isolated towns near glyphic ruins or sites of divine trauma. He is now a Grayhand — an autonomous operative of The Order, trained in glyph theory, glyph catalysis, and field manipulation of vulnerable populations.",
        "current_status": [
            "Sergeth does not hold any official title or authority within the Temple of the 3rd Strand.",
            "He resides in temporary quarters granted access to the temple’s sub-archives under an assumed scholarly title.",
            "His presence is tolerated due to his deep glyphic knowledge, rare manuscripts, and quiet demeanor.",
            "Most clergy believe he is a harmless eccentric, useful for his insight into glyph-nullification theory. A few suspect otherwise but lack evidence."
        ],
        "order_role": {
            "duties": [
                "Initiating glyph catalysis through torturous ritework",
                "Oversees scouting and selection of potential subjects, particularly orphaned or magically sensitive youth",
                "Keeps a secret record titled ‘The Failed Lights’ — names of those who perished under his care"
            ],
            "belief": "He does not relish his work, but believes it necessary to fulfill what The Order calls the lost inheritance of man."
        },
        "personality": {
            "voice": "Low, deliberate, often speaks in metaphors and rhetorical questions.",
            "demeanor": "Calm, patient, unhurried. Almost disturbingly detached from suffering unless provoked emotionally.",
            "quirks": [
                "Writes in copper ink",
                "Records everything not for memory, but for ritual",
                "Hums ancient battle hymns when alone"
            ]
        },
        "philosophy": "A will broken is still a shape. We just hammer it into function.",
        "secrets": [
            "Bears a glyph-scar on his chest: 'Whisper of Wills', which suppresses rebellious thoughts and emotional instability.",
            "Once spared a child marked for catalysis. That individual may now be an ally, spy, or curse.",
            "Suspects The Stranger is not merely a survivor — but the unbroken flame of the original Nobles. Sergeth fears, and perhaps even worships, what the Stranger might become."
        ],
        "narrative_hooks": [
            "May offer insight to PCs in exchange for fragments of glyph lore or relics. Speaks as a mentor, though never fully honest.",
            "Can provide information, but may turn on the party if they hinder The Order’s long-term plans.",
            "In moments of collapse, Sergeth may seek atonement — or offer himself as a final sacrifice to preserve a greater glyph truth."
        ],
        "appearance": {
            "name": "Sergeth the Gray",
            "alias": "The Gray Archivist, Whisper of Lost Threads",
            "gender": "Male",
            "age": "Appears mid-50s (true age unknown)",
            "species": "Half-Elf (or altered human)",
            "height": "5'10\" (178 cm)",
            "build": "Lean and brittle-looking, like a book that shouldn’t still hold together",
            "eyes": "Washed-out silver with a cloudy sheen; difficult to read, like a faded page",
            "hair": "White-gold and thinning, swept back in loose strands, often dusted with ash or ink",
            "skin": "Pale and drawn tight over high cheekbones, like parchment left out in wind",
            "voice": "Soft, deliberate, resonant with something unnatural—like a question echoing in an empty hall",
            "clothing": "Ash-gray robes layered over reinforced travel garb, stitched with forgotten glyphs; cuffs stained with copper ink",
            "accessories": "Carries a glyph-scarred journal, writes with a copper-nibbed quill; a single glyph medallion rests coldly against his sternum",
            "aesthetic": "Worn scholar of ruin; unsettling calm draped in forgotten wisdom",
            "aura": "Like standing near something that remembers too much—quiet, but heavy",
            "presence": "Commands attention not through power, but through silence that dares you to speak",
            "scent": "Faint scent of moldy vellum, sealing wax, and bitter herbs; often hums forgotten battle hymns under breath",
        },
    },
    "Maela Stonebraid": {
        "name": "Maela Stonebraid",
        "title": "Priestess of the 2nd Strand Temple in Aracine",
        "race": "Mountain Dwarf",
        "age": "Late 80s (appears early 60s by dwarf standards)",
        "background": "Maela Stonebraid is a veteran of Aracine’s Watch Guard, having served nearly five decades in roles ranging from street patrol to captaincy of the Lower District. After a celebrated but quietly political retirement, she accepted a spiritual calling and became the priestess of the Temple of the 2nd Strand, where she now leads rituals in honor of Vestal Dagmar (Earth – Loyalty). Known for her incorruptible sense of justice, pragmatic leadership, and quiet empathy, Maela commands deep respect from both the local garrison and the townsfolk of the Lower District.",
        "personality_traits": [
            "Calm and deliberate, speaks only when necessary",
            "Deeply loyal to the people of Aracine, especially the working class",
            "Holds unspoken authority even when not wearing armor"
        ],
        "motivations": [
            "Protect the people of Aracine from both spiritual and political dangers",
            "Maintain the independence and integrity of the Temple of the 2nd Strand",
            "Monitor imperial overreach and corruption discreetly"
        ],
        "known_publicly": [
            "Served with distinction in the Watch Guard",
            "Led several defensive actions during bandit incursions two decades ago",
            "Known to have turned down noble patronage in favor of community service",
            "Recently took priestly vows and assumed leadership of the 2nd Strand Temple",
        ],
        "secrets": [
            "Keeps a hidden network of trusted informants among the Lower District artisans and guilds",
            "Believes something is deeply wrong with the spiritual energy surrounding Aracine",
        ],
        "role_in_campaign": "Maela can serve as a moral compass, mentor, or reluctant conspirator. She may aid the players if they prove themselves aligned with community values or uncover threats to the balance between faith, empire, and forbidden glyphcraft. She will not tolerate manipulation or betrayal and is unlikely to forgive abuse of authority.",
        "appearance": {
            "name": "Maela Stonebraid",
            "alias": "The Iron Hearth, Sentinel of the Lower Temple",
            "gender": "Female",
            "age": "Late 80s (appears early 60s by dwarf standards)",
            "species": "Mountain Dwarf",
            "height": "4'6\" (137 cm)",
            "build": "Sturdy and thick-shouldered, like carved basalt",
            "eyes": "Deep brown with a grounding steadiness; unreadable yet warm",
            "hair": "Braided iron-gray with copper threads woven through; usually coiled in a disciplined bun",
            "skin": "Earth-toned and tough, marked with the faded lines of old patrol scars",
            "voice": "Low and grounded, like a drumbeat through stone; speaks with deliberate economy",
            "clothing": "Wears layered robes over repurposed guard armor; earth-toned vestments with 2nd Strand insignia (Dagmar – Loyalty) at the chest",
            "accessories": "Keeps a carved prayer-stone around her neck and a ceremonial war gauntlet strapped to one hip",
            "aesthetic": "Unshakable matron-sentinel—equal parts shrine and shield",
            "aura": "Invokes a quiet respect, as if her approval alone could sanctify a space",
            "presence": "Her silence often says more than others' speeches; crowds part for her without command",
            "scent": "Carries the scent of old oil, iron filings, and incense ash; gaze sharpens notably around corrupt officials",
            "description": "Maela Stonebraid is the Lower District’s quiet bastion—unmoved by politics, uncorrupted by power. Her dwarven frame, thick with veteran strength, now supports the vestments of a priestess, but she moves like a guard who never truly sheathed her blade. To the working people of Aracine, her word is law and her eyes are sanctuary. She bears no crown, but her authority is older than most noble lines. When Maela speaks, it’s to anchor a community—or to warn those who would fray it.",
        },
    },
    "Kiren Vell": {
        "name": "Kiren Vell",
        "title": "Fence, Smuggler, Black Market Guide",
        "race": "Half-Elf",
        "age": "36",
        "pronouns": "He/Him",
        "current_location": "Lower District, Aracine",
        "known_affiliations": "None officially, but rumored connections to underworld networks",
        "overview": "Kiren Vell operates as an illicit fixer in the lower districts of Aracine, moving goods, people, and secrets through the city’s overlooked alleys and forgotten basements. His skill in circumventing local law enforcement and the watchful eyes of the Myacene Goliaths makes him an indispensable contact for those seeking discretion. While he keeps a low profile, his knowledge of underground paths and covert logistics is unrivaled in the town.",
        "public_knowledge": [
            "Former quartermaster for a Goliath regiment, dishonorably discharged.",
            "Can secure off-the-books passage out of Aracine—for the right price.",
            "Frequently seen at *The Kettle’s Hook*, an inn with a private cellar.",
        ],
        "private_knowledge": [
            "Once smuggled rare magical components to unknown clients with glyph-etched crates—he discontinued the work after a near-fatal encounter.",
            "Has heard rumors of *The Order* and believes them real, but considers them too dangerous to engage with.",
            "Keeps an enchanted escape route warded through a collapsed passage behind the Guard Barracks.",
        ],
        "role_in_campaign": "Kiren serves as an optional but powerful tool for PCs attempting to escape Aracine or operate outside official systems. He provides narrative flexibility, introduces hints about The Order, and adds stakes to the underworld politics beneath Aracine’s polished veneer.",
        "notable_quotes": [
            "People don’t disappear in Aracine. They just stop being mentioned.",
            "You want to slip through the cracks? Then stay quiet, pay fast, and don’t ask about the crates with blood runes.",
            "I used to laugh at ghost stories. Until one of them stared back.",
        ],
        "appearance": {
            "name": "Kiren Vell",
            "alias": "The Ledgerless, Night-Runner of Aracine",
            "gender": "Male",
            "age": "36",
            "species": "Half-Elf",
            "height": "6'0\" (183 cm)",
            "build": "Wiry and quick, with a smuggler’s agility",
            "eyes": "Pale amber, sharp and always scanning for exits",
            "hair": "Black, shoulder-length, typically tied back in a rough tail or tucked under a hood",
            "skin": "Weathered tan, freckled with old burns and knife-nicks",
            "voice": "Dry, smooth, often laced with sardonic calm",
            "clothing": "Patchwork leathers, road-dusted cloak, always wears layers for concealment; boots reinforced with silent soles",
            "accessories": "Carries a hidden blade in his boot, a copper-threaded satchel with decoy compartments, and an enchanted ring that masks glyph traces",
            "aesthetic": "Shrouded edgewalker; danger tucked into casual shrug",
            "aura": "Carries the chill of someone who’s seen too much and survived anyway",
            "presence": "Easily overlooked in a crowd—until he chooses not to be",
            "scent": "Smells faintly of smokeleaf, tallow, and riverstone; fingers constantly in motion—tapping, flicking, counting",
            "description": "Kiren Vell moves like someone who’s always halfway to vanishing. His half-elven blood grants him a touch of grace, but it's buried beneath the grime of alley ash and the tension of too many secrets. He rarely meets a gaze for long unless he’s gauging what it’ll cost to betray you—or if it’s worth helping you escape. Old Goliath regimental tattoos linger faded under his sleeves, and his voice holds the ghost of someone who once had command, now traded for shadows. In Aracine’s forgotten alleys, his name opens doors... or closes them permanently.",

        },
    },
    "High Artificer Maelen Trost": {
        "name": "High Artificer Maelen Trost",
        "title": "Head of the 3rd Strand Temple in Aracine",
        "race": "Dwarf",
        "age": "143",
        "pronouns": "He/Him",
        "alignment": "Lawful Good",
        "affiliation": "Temple of the 3rd Strand (Vestal Seth – Metal, Righteousness)",
        "position": "Head of the 3rd Strand Temple in Aracine",
        "titles": ["Keeper of the Golden Litany", "Chainwarden of Purity", "High Artificer of Seth's Will"],
        "background_summary": "Maelen Trost hails from the Tavermount Mountains, south of Aracine — a region famed for its metallurgical schools and forge-priests devoted to the 3rd Strand. His early years were forged (quite literally) in these high sanctums, where the teachings of Righteousness as Form guided both spiritual and smithing disciplines. He was assigned to Aracine decades ago, a politically quiet post that nonetheless required theological authority and firm-handed stability. While not a major center of doctrine, Aracine’s temple still plays a critical regional role in maintaining public alignment with Vestal Seth’s teachings, particularly in matters of law, oaths, and glyph restriction.",
        "public_persona_and_duties": [
            "Leads rituals and oaths centered around righteousness, repentance, and judgment.",
            "Oversees a modest reliquary containing pre-war glyph relics and fragments believed to originate from early Noble usage.",
            "Respected as a neutral figure in disputes between guilds, clergy, and town council.",
            "Occasionally consults with Finn Valorian, but avoids becoming embroiled in town governance."
        ],
        "personality_profile": {
            "speech": "Steady and direct; apt to use forge analogies when discussing character or justice.",
            "demeanor": "Reserved and measured, rarely boasts or speaks without purpose.",
            "mannerisms": "Carries a ceremonial inscription hammer, which he taps rhythmically when deep in contemplation.",
            "philosophy": "Righteousness without pressure is untempered ore."
        },
        "narrative_role": {
            "moral_compass_or_judge": "Offers the players insight into the 3rd Strand’s beliefs and laws, especially regarding glyphic conduct.",
            "gatekeeper": "Might control access to glyphic relics or temple archives, requiring earned trust to proceed.",
            "limited_perspective": "Despite his wisdom, Maelen’s worldview is shaped by ritual and law — he does not know of the Order’s existence, and believes such conspiracy theories are dangerous fictions.",
            "potential_catalyst": "If the party exposes Order-related truth, Maelen may struggle to reconcile it with his faith and institutional blind spots."
        },
        "secrets": [
            "Possesses a counterglyph scroll known as The Severing Brand — designed to dispel glyphic influence from individuals, but only meant for sanctioned use by temple Inquisitors.",
            "Unaware of Sergeth’s true affiliation, though he considers the man ‘disquieting’ and keeps his access to temple spaces tightly restricted.",
            "Has seen one glyph sigil in the reliquary subtly shift its pattern in the presence of The Stranger — but he has not yet made sense of it."
        ],
        "appearance": {
            "name": "High Artificer Maelen Trost",
            "alias": "Keeper of the Golden Litany, Chainwarden of Purity",
            "gender": "Male",
            "age": "143",
            "species": "Dwarf",
            "height": "4'9\" (145 cm)",
            "build": "Broad and compact, with the solidity of a living anvil",
            "eyes": "Bronze-gold, steady and always calculating, like cooling metal",
            "hair": "Iron-gray, combed back into a short braid; thick brows, singed at the ends from forge sparks",
            "skin": "Ruddy from heat exposure, marked with minor ritual burns and hammer-calloused hands",
            "voice": "Deep and deliberate, like a hymn spoken over steel",
            "clothing": "Forgemaster’s robes reinforced with chain-lined hems; vestments etched with the sigils of Vestal Seth; always wears his inscribed ceremonial hammer at his hip",
            "accessories": "Gilded bracers marked with the three laws of metalwork and morality; a pendant containing a shard of pre-schism alloy",
            "aesthetic": "Forge-hardened sanctity; clean lines, no excess",
            "aura": "Measured intensity, like a sealed furnace that only opens when needed",
            "presence": "Quietly dominant—commands respect without needing volume",
            "scent": "Smells faintly of soot, molten ore, and incense; taps his hammer against his bracer when lost in thought",
            "description": "Maelen Trost is the embodiment of the 3rd Strand's creed: Righteousness as Form. His every movement is calculated and deliberate, like the setting of a rivet. Though his age is visible in the silvering of his beard and the weathering of his skin, his frame remains unbent by time or doubt. He is not just a priest but a forgemaster of doctrine, tempering both metal and morality in the same fire. In his presence, even truth feels weighed on scales—and found wanting if unrefined.",
        },
    },
    "Finn Valorian": {
        "name": "Finn Valorian",
        "title": "Civic Administrator of Aracine",
        "race": "Half-Elf",
        "apparent_age": "Mid-30s",
        "alignment": "Neutral Good (in conflict)",
        "strand_affiliation": "Officially aligned with the 2nd Strand (Earth/Loyalty), though only loosely practicing",
        "residence": "Town Hall Quarters, Market Square",
        "pronouns": "He/Him",
        "public_persona": "Finn is the visible face of governance in Aracine, a well-educated bureaucrat who believes in the ideals of civic responsibility and humane leadership. Unlike Alinary, he often walks the streets, speaks with townsfolk, and makes personal appearances at local events. His charisma earns loyalty, but his lack of forceful enforcement often frustrates the Goliath Watch and noble circles.",
        "public_reputation": [
            "Kind-hearted and pragmatic, often mediating disputes personally.",
            "A bit too soft for some of the harder edges of Aracine politics.",
            "Known for sponsoring public projects, including repairs, food support, and schoolbooks."
        ],
        "private_truths": [
            "Finn once trained under a Sigil Covenant cleric before leaving the temple over a doctrinal dispute — he still keeps the notes.",
            "He has seen glyphwork before — carved into the bones of a dying refugee — and carries that trauma privately.",
            "He believes The Stranger may be a lost Keeper relic, but fears saying so out loud without proof.",
            "Alinary has threatened him subtly in the past; he maintains a secret ledger detailing her questionable orders, but hasn’t yet decided if it’s a shield or a sword."
        ],
        "personality_traits": [
            "Idealistic but eroding. He wants to believe in institutions even as they disappoint him.",
            "Feels outmatched by the political weight of the Upper District, and often seeks quiet counsel from Sister Maela.",
            "Has a habit of asking rhetorical questions to buy time in tense meetings."
        ],
        "plot_hooks_and_interactions": [
            "If the PCs gain prominence, Finn may ask for their help investigating irregular Watch activity or old glyphic symbols appearing near the Market Square.",
            "If he’s exposed to the Stranger’s glyphs, he may unlock suppressed memories or become afflicted by arcane echoing (roleplay paranoia or visions).",
            "If Alinary moves against him, Finn may go into hiding — or foolishly attempt a political coup using the PCs’ influence.",
            "He can be a moral fulcrum for the party: helping them decide whether to ally with empire, temple, or glyph."
        ],
        "appearance": {
            "name": "Finn Valorian",
            "alias": "Civic Steward of Aracine",
            "gender": "Male",
            "age": "~70 (appears mid-30s)",
            "species": "Half-Elf",
            "height": "5'11\" (180 cm)",
            "build": "Lean with a scholar’s frame; resilient, but not hardened",
            "eyes": "Green-hazel, edged with quiet weariness and empathy",
            "hair": "Chestnut brown, touched faintly with silver at the temples; usually tied back or wind-brushed",
            "skin": "Light olive, with the faintly ageless tone common to half-elves",
            "voice": "Clear, resonant, often low in volume but full of nuance",
            "clothing": "Simple but well-tailored civic attire—longcoat, vest, and scarf in muted Aracine greens and bronzes",
            "accessories": "Keeps a leather-bound field ledger, quill case, and a concealed civic medallion marked with the Valorian seal",
            "aesthetic": "The balance between quiet confidence and lived vulnerability",
            "aura": "A subtle steadiness; people speak more carefully when he's in the room",
            "presence": "Disarming; he listens more than he speaks, and when he speaks, it stays with you",
            "scent": "A soft, clean scent of clove, waxed parchment, and weathered leather",
            "description": "Though Finn Valorian looks barely older than a promising human statesman, he carries himself with the calm and patience of someone who has lived twice as long. His half-elven blood has preserved his youth, but not spared him from the emotional toll of decades spent wrestling with systems too large to fix. He walks the streets of Aracine not as a ruler, but as a servant trying not to drown in compromise. Thoughtful, soft-spoken, and weighed down by truths he dare not name, Finn is both a symbol of hope and a man nearing the edge of disillusionment.",
            },
       },
    "Captain Rhendak Morvane": {
        "name": "Captain Rhendak Morvane",
        "title": "High Captain of the Aracine Watch",
        "race": "Goliath",
        "apparent_age": "Late 40s (for a Goliath; mature, battle-worn)",
        "strand_affiliation": "Nominally loyal to the 2nd Strand (Earth/Loyalty), but not doctrinal",
        "pronouns": "He/Him",
        "alignment": "Lawful Neutral (Authoritarian, with tribal memory)",
        "public_persona": "Rhendak is a formidable and respected figure, both feared and admired in equal measure. He commands the Myacene Goliath Watch, a force known for rigid discipline and absolute loyalty. His presence at a public event often signals one of two things: a show of power, or the imminent enforcement of policy.",
        "public_reputation": [
            "Unshakeable, intimidating, and rarely emotional.",
            "A living relic of the Goliath campaigns against Avatar, covered in ritual scars.",
            "Known for siding with order above mercy, but also for protecting those under his banner without hesitation."
        ],
        "private_truths": [
            "Rhendak despises nobles in private — including Alinary — though he will never say it aloud. His loyalty is to Aracine as a place, not its rulers.",
            "He once served as a warden at a glyph-quarantine fortress, and bears silent trauma from the experience — including a disfigurement along his ribs, covered by ritual inks.",
            "He keeps coded scrolls in his personal quarters referencing incidents the empire has tried to erase — including glyph-bearing prisoners who 'vanished.'",
            "Secretly believes The Stranger is a contagion — not divine, not evil, but something that will bring death in its wake if not monitored or purged."
        ],
        "personality_traits": [
            "Speaks plainly and without euphemism; rituals of conversation bore him.",
            "Treats soldiers as kin but holds outsiders at arm’s length until proven.",
            "Deeply superstitious, despite his rational exterior — he will not camp near temple ruins or touch ancient glyphs."
        ],
        "plot_hooks_and_interactions": [
            "May oppose the PCs if they defy curfew or become involved in any glyph-related events — especially without first going through 'proper channels.'",
            "Could be convinced to share details about the glyph-quarantine outposts or lost prisoners, if players gain his respect.",
            "Might request the party help interrogate a glyph-afflicted deserter brought in silently to the barracks — providing moral and strategic conflict.",
            "If tensions escalate, Rhendak might side with neither Alinary nor Finn, but attempt to militarize the Watch and establish martial law — believing Aracine’s survival depends on it."
        ],
        "appearance": {
            "name": "Captain Rhendak Morvane",
            "alias": "The Stonebrand, High Captain of the Watch",
            "gender": "Male",
            "age": "Late 40s (Goliath years)",
            "species": "Goliath",
            "height": "7'2\" (218 cm)",
            "build": "Towering and broad-shouldered; every inch carved like a siege engine",
            "eyes": "Storm-dark with a perpetual squint, as if weighing every soul",
            "hair": "None; scalp and jawline bear ceremonial tattoos and scarification",
            "skin": "Granite-hued with black marbling; his ritual scars glow faintly under certain lights",
            "voice": "Deep and gravelly, like stone dragged across steel",
            "clothing": "Functional plated armor etched with the sigils of old Goliath regiments and the Earth Strand; cloak of cracked leather, worn and unadorned",
            "accessories": "Carries a war baton engraved with ancestral marks; several rings made of hardened bone and bronze",
            "aesthetic": "Impenetrable presence—like a monolith come to life",
            "aura": "Commands obedience without shouting; silence deepens in his wake",
            "presence": "Instinctively creates space in a room; others avoid standing behind him out of sheer respect",
            "scent": "Faint scent of cold iron and scorched earth; his steps echo louder than they should",
            "description": "Captain Rhendak Morvane is the embodiment of Aracine’s will made flesh—an immovable force who speaks rarely but with absolute finality. His battle-worn body is a map of the Goliath wars, with inked scars crossing his chest and ribs, partially hidden beneath layers of disciplined armor. Though he enforces law with a clenched fist, his gaze carries a deeper pain—one earned in glyphic quarantine halls and field pyres. Rhendak is no tyrant, but he is no savior either. He is the last wall, and he knows it.",
        },
    },
    "Alinary Digiverny": {
        "name": "Lady Alinary Digiverny",
        "title": "Lady of Aracine, Holder of Land Decree 17-Exarch",
        "race": "Human",
        "apparent_age": "Early 40s",
        "strand_affiliation": "None officially declared (privately sympathetic to 3rd Strand philosophy)",
        "residence": "Estate atop the Upper District ridge",
        "pronouns": "She/Her",
        "alignment": "Lawful Neutral (Veiled agendas)",
        "public_persona": "Lady Alinary Digiverny presents herself as an elegant, unflinching bureaucrat, more noble by edict than by legacy. She is deeply committed to maintaining order through law, reputation, and ritual symbolism, often leaning on the aesthetics of power rather than overt shows of it.",
        "public_reputation": [
            "A distant yet competent authority, more inclined to dispatch representatives than meet commoners directly.",
            "Uninvolved in temple doctrine, but protective of religious institutions that serve the empire’s interests.",
            "Hostile to unsanctioned magic, particularly that which is glyphic, prophetic, or divine in nature."
        ],
        "private_truths": [
            "Alinary hoards pre-schism artifacts from before the sacrifice of Bjorn — her estate includes locked vaults containing glyphwork panels, fragments of old Keeper scripts, and an encoded steel reliquary she has never been able to open.",
            "She has made two secret correspondences with Avatarian diplomats in the past three years, hoping to stabilize tensions through artifact trade.",
            "She suspects Finn Valorian is concealing glyph-related incidents and is considering replacing him with a loyal officer from another town.",
            "She believes The Stranger is a living glyph-key, and may be quietly directing temple resources to monitor him from a distance.",
            "She is a member of “The Circle”, a secret organization that holds court in an underground assembly chamber of polished obsidian below the Digiverny Estate known to its members as “The Estate of Masks”."
        ],
        "personality_traits": [
            "Speaks in layers, preferring double-meaning and veiled expectations.",
            "Rarely shows anger, but delivers disappointment like a scalpel.",
            "Maintains a ceremonial persona even in private, rarely unguarded."
        ],
        "plot_hooks_and_interactions": [
            "The PCs may be summoned by Alinary under false pretenses — e.g., to test their moral fiber in handling a glyph incident without knowing it’s her artifact.",
            "If The Stranger gains public favor, Alinary may attempt to co-opt or imprison him under empire-sanctioned protection orders.",
            "If the players unearth too much about Bjorn’s fragmented will, Alinary may resort to political manipulation or assassination by proxy.",
            "A deal could be offered: access to a glyph relic vault in exchange for silencing a whisper campaign about her involvement in forbidden research."
        ],
        "appearance": {
            "name": "Lady Alinary Digiverny",
            "alias": "The Lady of Aracine",
            "gender": "Female",
            "age": "Early 40s (apparent)",
            "species": "Human",
            "height": "5'9\" (175 cm)",
            "build": "Slender, statuesque",
            "eyes": "Steel gray, sharp and calculating",
            "hair": "Ash-blonde, coiled into elaborate braids wrapped with silver thread",
            "skin": "Pale ivory with a porcelain-like stillness",
            "voice": "Low and precise, each word sculpted for impact",
            "clothing": "Layered noble garb in muted empire blues and shadow-gray; high collars, ornamental cuffs, and embroidered strands symbolizing power and law",
            "accessories": "Silver signet ring bearing the crest of Digiverny; jeweled brooch shaped like a closed eye; ceremonial key pendant",
            "aesthetic": "Regal austerity—like a portrait come to life, unmoved by wind or time",
            "aura": "A chill of veiled judgment; those near her feel subtly measured",
            "presence": "Commands a room without raising her voice; gestures spare but intentional",
            "scent": "Faint scent of ink, myrrh, and parchment lingers in her wake",
            "description": "Lady Alinary Digiverny embodies the elegance of empire-bound law cloaked in silence and scrutiny. Her posture is unyielding, as if gravity dares not disrespect her spine. She rarely blinks when spoken to, and her gaze carries the weight of unspoken consequences. Though untouched by obvious magic, she exudes the authority of someone who has studied power—both ancient and political—and keeps its relics behind locked doors.",
        },
    },
}

@app.get("/npcs", response_model=List[str])
def list_npcs():
    return list(npcs.keys())

@app.get("/npcs/{name}")
def get_npc(name: str):
    if name not in npcs:
        raise HTTPException(status_code=404, detail="NPC not found")
    return npcs[name]
