from models import Location

raw_locations = {
    "aracine": Location(
        name="Aracine",
        type="Fortified Town",
		region="Agasan",
		population="~10,000",
		description=(
			"A fortified town bridging imperial power and local identity, Aracine serves as a cultural and strategic nexus. "
			"Positioned along a key trade artery between the Tavermount Mountains and the inland cities of Agasan, it is a place of watchful silence, divine echoes, and unsaid truths. "
			"Religious factions, noble dictates, and smuggled heresies all share its stonework."
		),
		geography={
			"Upper District: A raised, walled sector housing temples, noble estates, and military command. Rigidly controlled and symbolically imperial.",
			"Lower District: The city's pulsing heart — markets, shrines, and mingled lives beneath the watch of weary guards and older laws.",
		},
		sublocations=[
			"Temple of the 3rd Strand",
			"Temple of the 2nd Strand",
			"Alinary’s Estate",
			"Guard House (Upper)",
			"Guard Barracks (Lower)",
			"Market Square",
			"Southgate Hollow",
			"The Bronze Tankard",
			"The Kettle’s Hook",
			"The Adamantine Walk",
		],
		factions_present=[
			"The Order",
		],
		religious_sites=[
			"Temple of the 3rd Strand",
			"Temple of the 2nd Strand",
		],
		associated_npcs=[
			"Alinary Digiverny",
			"Finn Valorian",
			"Captain Rhendak Morvane",
			"Priestess Maela Stonebraid",
			"High Artificer Maelen Trost",
			"Sergeth the Gray",
			"Kiren Vell",
		],
		secrets=[
			"Temple of the 3rd Strand has been infiltrated by The Order.",
			"The Kettle’s Hook contains a hidden speakeasy under its cellar.",
			"A hidden containment structure called the Blackrock Compact is located under the 2nd strand temple",
		],
		notable_features=[
			"The Adamantine Walk – ceremonial route for decrees and noble processions",
			"Tensions between religious law and glyphic heresy",
			"Unseen glyphic remnants buried beneath both districts",
		],
        aliases= None,
	),
    "glaemors_hollow": Location(
        name="Glaemor’s Hollow",
        type="Subterranean Hamlet",
        region="The Northern Gales",
        population="~800 (mostly dwarves and weather-shunned outcasts)",
        description=(
            "Glaemor’s Hollow lies beneath the frost-riven plateaus of the Northern Gales, a cavern-hamlet warmed by geothermal steam. "
            "Built within obsidian-hewn crevices, its residents harvest cave silk and frost salts while fending off the psychological toll of long auroraic exposure. "
            "Memory echoes sometimes dance across the walls, whispering half-truths into dreams."
        ),
        geography={
            "Steamshaft Bazaar: A multilevel chamber filled with stalls built around fumaroles, rich in trade and hallucinated rumors.",
            "The Whispered Hall: An old vault of carved runes where voices speak from the stone.",
        },
        sublocations=[
            "Steamshaft Bazaar",
            "The Whispered Hall",
            "Saltbrewer's Tap",
            "Hearthcrack Shrine",
            "Frostwatch Gate",
        ],
        factions_present=[
            "Silent Archive",
        ],
        religious_sites=[
            "Hearthcrack Shrine",
        ],
        associated_npcs=[
            "Archivist Belven Noorr",
            "Warden Thaleen Dravik",
            "Elleran the Skald",
        ],
        secrets=[
            "A sealed corridor behind the Whispered Hall contains glyphs etched in frost that burn the eyes of readers.",
            "Elleran’s songs are encoded warnings from a lost Silent Archive scribe.",
        ],
        notable_features=[
            "Aurora-stained ice formations that mimic past conversations.",
            "A floating shard of unmelting snow rumored to be a failed glyph construct.",
        ],
        aliases=None,
    ),
    "trithling_cradle": Location(
        name="Trithling Cradle",
        type="Migratory Trade Assembly",
        region="Windplain Arch",
        population="Varies (2,000–5,000 during peak convergence)",
        description=(
            "Each spring, the nomadic clans of the Windplain Arch converge at the Trithling Cradle—a shifting camp of collapsible towers and storm-etched banners. "
            "Here, traditions are reforged, blood feuds settled, and wind-scribed contracts sung into being. "
            "It is equal parts market, council, and battlefield—where thunder answers truth."
        ),
        geography={
            "Stormring Hall: A great open-air arena where lightning duels and truth-vows are enacted.",
            "The Chorus Vales: Wind-carved dales where songsmiths barter verse for vision.",
        },
        sublocations=[
            "Stormring Hall",
            "The Chorus Vales",
            "Ancestral Emberstone",
            "The Spiral Forge",
        ],
        factions_present=[
            "Avatar Dominion",
        ],
        religious_sites=[
            "Ancestral Emberstone",
        ],
        associated_npcs=[
            "Storm-Speaker Narei Kael",
            "Tamin of the Skyspool",
            "Rhava Emberblight",
        ],
        secrets=[
            "One of the wind-chants recited during the Trithling contains a hidden glyph of directional memory.",
            "A rogue Avatar Ritual Knight uses the Spiral Forge to craft illegal glyph-metal javelins.",
        ],
        notable_features=[
            "Storm-chariots leave trails of crackling light.",
            "Wind echoes carry the voices of ancestors, sometimes contradicting history.",
        ],
        aliases=["The Meeting Gale", "Thunder’s Law"],
    ),
    "the_hollow_canticle": Location(
        name="The Hollow Canticle",
        type="Sunken Monastic Vault",
        region="Sunken Thread",
        population="Unknown (rumored caretakers: <100)",
        description=(
            "The Hollow Canticle rests submerged beneath the reefs of the Aemil Reach, an ancient monastery whose bells are said to still toll underwater. "
            "The surviving clergy speak only in verse and pass knowledge through echo-rituals woven in chant. "
            "It is warded by harmonic glyphs known only to the Sigil Covenant’s innermost circle."
        ),
        geography={
            "Echocrypt Walk: A submerged hall of memory-mirrors where speech fractures into harmony.",
            "Brine-Spires: Towering coral libraries grown around glyph-tuned resonance.",
        },
        sublocations=[
            "Echocrypt Walk",
            "Brine-Spires",
            "The Mute Chapel",
            "The Numb Archive",
            "Glimmervault Seal",
        ],
        factions_present=[
            "Sigil Covenant",
        ],
        religious_sites=[
            "The Mute Chapel",
        ],
        associated_npcs=[
            "Archbind Soreil Keth",
            "Curate-Lurien",
            "Warden Bellarid",
        ],
        secrets=[
            "The Mute Chapel contains a glyph that can suppress heretical dreams across an entire region.",
            "The Glimmervault Seal hides a relic linked to the Forbidden Sixth Strand.",
        ],
        notable_features=[
            "The bells toll even with no visible mechanism.",
            "No song survives unchanged after being sung within the Canticle.",
        ],
        aliases=["Drowned Choir", "The Mouthless Temple"],
    ),
    "salkirs_moor": Location(
        name="Salkir’s Moor",
        type="Shrouded Refuge",
        region="The Northern Gales",
        population="Approx. 850 (including non-speaking exiles)",
        description=(
            "Hidden within a steaming glacial fissure, Salkir’s Moor is a settlement of fog-veiled platforms, obsidian towers, and mirrored sanctuaries. "
            "Founded by those cast out for truths no one wanted spoken, the town is governed by a Pact of Silence — broken only in rites overseen by the Veil Shepherds. "
            "Every building is connected by heat-conducting bridgeways powered by buried echo-cores, their origin unknown even to the oldest wardens."
        ),
        geography={
            "Steamglass Halls: Condensation-veiled passageways where mirrors distort not just reflections but memory.",
            "Frost-Thorn Pillars: Jagged mineral extrusions riddled with runic scars, radiating faint warmth.",
            "Echocoil Basin: A thermal lake whose surface reflects events minutes before they occur.",
        },
        sublocations=[
            "Steamglass Halls",
            "Frost-Thorn Pillars",
            "Echocoil Basin",
            "The Drowned Library",
            "Pactstone Hollow",
        ],
        factions_present=[
            "Wardens of the Fissure",
            "Veil Shepherds",
        ],
        religious_sites=[
            "Pactstone Hollow",
        ],
        associated_npcs=[
            "Matron Selwyn Ashlim",
            "Cipher-Twin Ellun & Drel",
            "Warder Kael Morven",
        ],
        secrets=[
            "The Echocoil Basin is believed to be a glyph-breach echoing backward from an unresolved future.",
            "The Pact of Silence is enforced not by law, but by a memetic curse tied to the mirrored hallways.",
        ],
        notable_features=[
            "No song or speech carries farther than a few feet — as if the air swallows intent.",
            "Mirrors here fog over only when approached by liars.",
        ],
        aliases=["The Quiet Furnace", "Veilhold"]
    ),
    "tel_varuun": Location(
        name="Tel Varuun",
        type="Living Canopy Commune",
        region="The Verdant Veins",
        population="Approx. 2,300 (excluding semi-sapient treants and dreambound spirits)",
        description=(
            "Suspended across the highest branches of the Loameaves — a colossal arboreal tangle older than the moonfall — Tel Varuun is a commune woven entirely from living vine, root, and song-carved bark. "
            "Its residents move between districts along root-bridges sung into growth by barkcant rituals. Rulership is seasonal and choral: five voices, one for each quadrant moon, harmonize law. "
            "Tel Varuun is both city and organism — a place where roots remember trespass, and every leaf may be listening."
        ),
        geography={
            "Verdant Spiral: A gently twisting arboreal tower coiled around a dreamseed crystal at its core.",
            "Rootsong Bridge: A living transit artery between canopy districts that shifts location at dawn.",
            "Canopy Archives: Layered leaf-domes whose interiors hold dream-pods encoded with ancestral memory.",
        },
        sublocations=[
            "Verdant Spiral",
            "Rootsong Bridge",
            "Canopy Archives",
            "The Mosslit Forum",
            "The Lamenting Bloom",
        ],
        factions_present=[
            "The Barkbound Choir",
            "Menders of the Loomleaf",
        ],
        religious_sites=[
            "The Lamenting Bloom",
        ],
        associated_npcs=[
            "Elder-Mender Vess'raen",
            "Chorus-Twin Kalai & Miren",
            "Dreamkeeper Ashwint",
        ],
        secrets=[
            "A sealed dreampod deep in the Archives contains memories from before the fall of the Fifth Strand.",
            "The Verdant Spiral's core is cracking — and humming the same tune every night without fail.",
        ],
        notable_features=[
            "All messages must be sung — written words wither within hours unless blessed.",
            "Certain trees in the commune bear faces: they belong to the Disremembered.",
        ],
        aliases=["The Highwoven Memory", "City of Singing Roots"]
    ),
    "drosven_hold": Location(
        name="Drosven Hold",
        type="Fortress Town",
        region="The Middle Kingdoms",
        population="Approx. 4,700 (excluding subterranean conscripts and invalids)",
        description=(
            "Once the final wall between the Middle Kingdoms and the Avataric Flood, Drosven Hold stands as both monument and warning. "
            "Its slate towers glint with mirrored alloy said to distort spell-aim, and the streets are paved with quarried memorial stone — each brick carved with the name of a fallen defender. "
            "Glyph-null wards were etched into its walls after the Siege of the Four Voices, rendering the Hold nearly impervious to magic… but not to memory."
        ),
        geography={
            "Crimson Ring: An arena-slash-tribunal where challenges to law are settled in armed rite.",
            "Wall of Names: A mile-long inner barrier engraved with the fallen — and, disturbingly, future names.",
            "Sanctum of Reversal: A warded vault whose glyphless blade unravels memory with each strike.",
        },
        sublocations=[
            "Crimson Ring",
            "Wall of Names",
            "Sanctum of Reversal",
            "The Bleeding Steps",
            "Lone Ember Chapel",
        ],
        factions_present=[
            "Ironcloaks",
            "The Fractured Chorus",
        ],
        religious_sites=[
            "Lone Ember Chapel",
        ],
        associated_npcs=[
            "Marshal Yerna Kulgrave",
            "Versewright Halred",
            "Sigil-Abjurer Brannet Vos",
        ],
        secrets=[
            "The Wall of Names updates itself — each midnight, a few new names appear in flawless script.",
            "The Sanctum blade 'Nullfang' is rumored to sever more than just memory — some say it carves fate.",
        ],
        notable_features=[
            "No arcane spells function within the Keep’s inner circle unless cast in blood.",
            "The Ember Chapel’s flame has never extinguished, though no fuel has ever been seen within.",
        ],
        aliases=["The Stone That Bled", "Nullhold"]
    ),
    "nhalms_wake": Location(
        name="Nhalm’s Wake",
        type="Amphibious Salt-City",
        region="The Sunken Thread",
        population="Approx. 3,900 (including drifting flotilla communes)",
        description=(
            "Anchored across a chain of salt-burnished platforms, bone-scaffold towers, and tide-hollowed hulls, Nhalm’s Wake drifts slow and sun-sick over the Siltglass Deep. "
            "Its people are born to brine and bell — raised by salt and silence, trained from infancy to swim the currents before ever walking its swaying decks. "
            "Governed by the Tide-Chained Court, rulings are rendered in bell-tolls and rhythmic tide-scripts, unreadable to landkind. Saltbone Diviners interpret dreams drowned in foam to dictate policy, punishment, and fate."
        ),
        geography={
            "Bone Wharf: A porous docking maze grown from maston vertebrae and storm-reeled shipwrecks.",
            "Undercurrent Chapel: Submerged temple accessible only during specific lunar ebbs.",
            "The Floating Forum: Drift-buoy council platform where bells ring language into law.",
        },
        sublocations=[
            "Bone Wharf",
            "Undercurrent Chapel",
            "The Floating Forum",
            "The Lanterned Graves",
            "The Brackish Coil",
        ],
        factions_present=[
            "Tide-Chained Court",
            "Saltbone Diviners",
        ],
        religious_sites=[
            "Undercurrent Chapel",
            "The Lanterned Graves",
        ],
        associated_npcs=[
            "Tide-Seer Oveline Marr",
            "Brinebell Warden Rethic",
            "Archivist Silvra Drown",
        ],
        secrets=[
            "The Wake's anchor-chain descends not to seafloor, but to an open mausoleum beneath the tide.",
            "Saltbone Diviners once summoned a spirit tide that now listens to every word spoken after dusk.",
        ],
        notable_features=[
            "Every home carries a bell tuned to a family’s bloodline.",
            "The city drifts slightly faster than the surrounding current — but no one knows why.",
        ],
        aliases=["The Drifting Wake", "City of Bells and Bone"]
    ),
    "skel_vanith": Location(
        name="Skel Vanith",
        type="Nomadic Bone-Town",
        region="The Windplain Arch",
        population="Approx. 1,100 (variable depending on wind-season caravans)",
        description=(
            "Built upon the skeletal remains of mastons long dead, Skel Vanith moves with the will of the wind — its structures lashed together with hide, sinew, and prayer-stitched cloth. "
            "Storm-wagons haul the town across the Windplain's sacred ley-paths, directed by the Galebound and judged by the Scorchhorn Riders. "
            "The town never stops for more than six days in any place; superstition claims stillness draws the Hollow Spiral. Justice is meted out by sky-duel, and every dwelling bears the tale of its owner in painted bone sigils."
        ),
        geography={
            "Hollow Mast Hall: Central longhouse of rib-bone and tanned skycloth where town rites are sung.",
            "Spine Market: A serpentine stretch of bartered relics, windglass, and sky-forged blades.",
            "Storm Docket Grounds: Trial field where duels are fought to the wind’s timing, not the blade’s.",
        },
        sublocations=[
            "Hollow Mast Hall",
            "Spine Market",
            "Storm Docket Grounds",
            "The Tether-Hooks",
            "Banner-Bone Grove",
        ],
        factions_present=[
            "The Galebound",
            "Scorchhorn Riders",
        ],
        religious_sites=[
            "Banner-Bone Grove",
        ],
        associated_npcs=[
            "Speaker-Orn Veln",
            "Chimebrand Isselka",
            "Dustwrest Kaul",
        ],
        secrets=[
            "The Grove’s oldest bone-banner weeps during certain eclipses — staining cloth with symbols no one recalls painting.",
            "The Tether-Hooks once lashed a floating city to the plains — it broke free, and some say it still circles above.",
        ],
        notable_features=[
            "Wind always arrives ten minutes before the town does — even in still weather.",
            "The town’s bones are engraved with maps that change slowly across seasons.",
        ],
        aliases=["Wind’s Spine", "The Roaming Judgment"]
    ),
}
