from models import NPC, Appearance


raw_npcs = {
    "sergeth_the_gray": NPC(
        name="Sergeth the Gray",
        title="Glyph Theorist in Residence",
        race="Half-Elf (or possibly altered human)",
        age="Estimated mid-50s (biological), unnaturally preserved",
        pronouns="He/Him",
        alignment="Neutral",
        affiliation="The Order (Grayhand Operative)",
        aliases=["The Gray Archivist", "Whisper of Lost Threads", "Fieldwalker of Quiet Tomes"],
        background=(
            "Once a scribe for the Sigil Covenant, Sergeth vanished from Agasan records three decades ago. "
            "Now a Grayhand — one of The Order’s independent agents — he operates in shadows and temples, "
            "tolerated only because of his unassailable insight into glyph nullification. His voice is low, his truths brutal, "
            "and his loyalty given not to people, but to purpose. He catalogues failures as one might blessings — meticulously, mournfully."
        ),
        overview="A withered scholar of terrifying purpose, bearing glyph scars in place of soul. He watches the world’s unraveling — and measures it.",
        appearance=Appearance(
            alias="The Gray Archivist, Whisper of Lost Threads",
            gender="Male",
            age="Mid-50s (apparent)",
            species="Half-Elf (or altered human)",
            height="5'10\" (178 cm)",
            build="Lean, brittle-looking, like a book too long handled",
            eyes="Washed-out silver, cloudy like forgotten vellum",
            hair="White-gold, swept back and thinning; often flecked with ash",
            skin="Taut and pale, like parchment pulled too tight",
            voice="Soft, deliberate, and echoing — like a question left unanswered",
            clothing="Ash-gray robes over fieldwear; cuffs ink-stained, glyph-threaded hems",
            accessories="Copper-nibbed quill, glyph-scarred journal, glyph medallion at sternum",
            aesthetic="Walking ruin of forgotten academia; a warning whispered in robes",
            aura="Like silence made heavy by history",
            presence="Draws attention by absence — dares others to break his quiet",
            scent="Old vellum, sealing wax, bitter herb; a ghost of memory",
            description=(
                "Sergeth is a scholar who should not still stand. He is memory carved in flesh, a man who records not for truth, "
                "but for use. His journals are not logs — they are spells of pattern. His kindness is untrustworthy. His silence, even worse."
            ),
        ),
        secrets=[
            "Bears a glyph-scar called 'Whisper of Wills' that suppresses rebellion and emotion.",
            "Keeps a journal titled ‘The Failed Lights’—a record of glyph catalysis deaths under his care.",
            "Believes the Stranger may be the last true Noble — or the final weapon forged from their broken line."
        ],
        motivations=[
            "Advance The Order’s glyphic reclamation, no matter the cost.",
            "Preserve the knowledge of what was lost, and what must not return.",
            "Find meaning in failure by making it repeatable — and survivable."
        ],
        weapons=None,
        known_publicly=[
            "Resides unofficially in the 3rd Strand Archives; tolerated for insight.",
            "Avoided by clergy, yet grudgingly consulted in crises."
        ],
        public_knowledge=[
            "Does not hold title, but answers glyph queries like a silent oracle.",
            "Feared for knowledge, not power — rarely seen in daylight."
        ],
        private_knowledge=[
            "Once spared a glyph-marked child. That child may now be ally, spy, or threat.",
            "May attempt atonement through death, betrayal, or sacrifice — depending on which truth cuts deepest."
        ],
        role_in_campaign=(
            "Sergeth can provide lore, access, or damning prophecy — for a price. His aid may save a soul or doom a mission. "
            "If cornered, he becomes either mentor or martyr — and the glyphs will write which."
        ),
        personality_traits=[
            "Detached, precise, and burdened by too much memory.",
            "Calm even during collapse — unless confronted by surviving light.",
            "Marks time by pen strokes and deaths he couldn’t prevent."
        ],
        narrative_hooks=[
            "Will trade insight for relics or memories the party barely understands.",
            "May betray the party if they threaten The Order’s deeper cause.",
            "Could beg them to finish what he cannot — burning himself for a final glyphic truth."
        ],
        plot_hooks_and_interactions=[
            "Linked to every failed glyphic catalyst in Aracine’s history.",
            "Knows of relics, locations, and patterns the clergy fear to whisper.",
            "Could unlock or suppress glyphs — or curse the user forever."
        ],
        notable_quotes=[
            "A will broken is still a shape. We just hammer it into function.",
            "Hope is not dangerous. Belief is. It makes the failed think they can rise.",
            "You think I'm the villain. No. I'm the historian. I just stopped pretending the past can be buried."
        ],
    ),
    "maela_stonebraid": NPC(
        name="Maela Stonebraid",
        title="Priestess of the 2nd Strand Temple in Aracine",
        race="Mountain Dwarf",
        age="Late 80s (appears early 60s by dwarf standards)",
        pronouns="She/Her",
        alignment=None,  # Not specified directly
        affiliation="Temple of the 2nd Strand",
        aliases=["The Iron Hearth", "Sentinel of the Lower Temple"],
        background=(
            "Veteran of Aracine’s Watch Guard, with nearly five decades of service from patrol to captain. "
            "Retired and later assumed the priesthood of the 2nd Strand, honoring Vestal Dagmar. "
            "She is a respected community leader, known for incorruptible justice and quiet authority."
        ),
        overview="A stalwart priestess and former guard captain whose presence sanctifies and shields.",
        appearance=Appearance(
            alias="The Iron Hearth, Sentinel of the Lower Temple",
            gender="Female",
            age="Late 80s (appears early 60s by dwarf standards)",
            species="Mountain Dwarf",
            height="4'6\" (137 cm)",
            build="Sturdy and thick-shouldered, like carved basalt",
            eyes="Deep brown with a grounding steadiness; unreadable yet warm",
            hair="Braided iron-gray with copper threads, coiled in a disciplined bun",
            skin="Earth-toned and tough, marked with the faded lines of old patrol scars",
            voice="Low and grounded, like a drumbeat through stone; speaks with deliberate economy",
            clothing="Layered robes over repurposed guard armor; earth-toned with Dagmar’s insignia",
            accessories="Carved prayer-stone necklace and ceremonial war gauntlet at her hip",
            aesthetic="Unshakable matron-sentinel—equal parts shrine and shield",
            aura="Quiet respect; her approval alone could sanctify a space",
            presence="Her silence speaks louder than others’ speeches; commands space without command",
            scent="Old oil, iron filings, incense ash; sharpens around corruption",
            description=(
                "Maela Stonebraid is the Lower District’s quiet bastion—unmoved by politics, uncorrupted by power. "
                "Her dwarven frame, thick with veteran strength, now supports the vestments of a priestess, but she "
                "moves like a guard who never truly sheathed her blade. To the working people of Aracine, her word is law "
                "and her eyes are sanctuary. She bears no crown, but her authority is older than most noble lines."
            )
        ),
        secrets=[
            "Maintains a hidden network of informants among Lower District artisans and guilds.",
            "Feels a deep spiritual disturbance in Aracine's glyphic fabric—fears it may relate to The Order."
        ],
        motivations=[
            "Protect Aracine’s people from both spiritual and political threats.",
            "Preserve the integrity of the 2nd Strand Temple.",
            "Watch imperial authority with quiet suspicion."
        ],
        weapons=None,
        known_publicly=[
            "Veteran guard captain of Aracine.",
            "Refused noble patronage to serve the community.",
            "Became priestess of the Temple of the 2nd Strand."
        ],
        public_knowledge=[
            "Leads rituals in honor of Vestal Dagmar.",
            "Respected by both the Watch Guard and local populace."
        ],
        private_knowledge=[
            "Her spiritual instincts sense a glyphic contamination.",
            "Mistrusts noble agendas and tracks temple politics carefully."
        ],
        role_in_campaign=(
            "Serves as a potential mentor, anchor, or resistance leader. "
            "Aligns with parties that value community, loyalty, and integrity. "
            "May become a crucial ally in opposing The Order or imperial overreach."
        ),
        personality_traits=[
            "Calm and deliberate; speaks only when necessary.",
            "Loyal to the working class of Aracine.",
            "Carries unspoken authority like a mantle."
        ],
        narrative_hooks=[
            "Can grant sanctuary, guidance, or relics of the 2nd Strand to worthy PCs.",
            "Will become an unshakable enemy if the party betrays community trust.",
            "Holds access to the Blackrock Compact and glyphic history."
        ],
        plot_hooks_and_interactions=[
            "Involved in Scene 2D’s reliquary arc.",
            "Can testify against corrupt nobility if convinced.",
            "Might reveal forbidden truths about Dagmar’s rites or The Order’s interference."
        ],
        notable_quotes=[
            "The Blackrock Compact. A safeguard... made by scribes who didn’t trust even themselves."
        ]
    ),

    "kiren_vell": NPC(
        name="Kiren Vell",
        title="Fence, Smuggler, Black Market Guide",
        race="Half-Elf",
        age="36",
        pronouns="He/Him",
        alignment=None,
        affiliation=None,
        aliases=["The Ledgerless", "Night-Runner of Aracine"],
        background=(
            "Once a quartermaster for a Goliath regiment, Kiren was dishonorably discharged under ambiguous circumstances. "
            "He resurfaced in Aracine as a covert fixer and smuggler, facilitating illegal movement of goods, fugitives, and magical contraband. "
            "Known for his knowledge of hidden paths and a reluctance to ask questions—if the coin is good enough."
        ),
        overview="A sardonic smuggler who moves secrets through shadows and drinks with ghosts.",
        appearance=Appearance(
            alias="The Ledgerless, Night-Runner of Aracine",
            gender="Male",
            age="36",
            species="Half-Elf",
            height="6'0\" (183 cm)",
            build="Wiry and quick, with a smuggler’s agility",
            eyes="Pale amber, sharp and always scanning for exits",
            hair="Black, shoulder-length, tied back or hooded",
            skin="Weathered tan, marked by burns and knife-nicks",
            voice="Dry, smooth, laced with sardonic calm",
            clothing="Patchwork leathers and road-dusted cloak; reinforced boots with silent soles",
            accessories="Hidden boot blade, decoyed satchel, glyph-masking enchanted ring",
            aesthetic="Shrouded edgewalker; danger tucked into casual shrug",
            aura="Carries the chill of someone who’s seen too much and survived anyway",
            presence="Easily lost in crowds—until he wants to be found",
            scent="Smokeleaf, tallow, riverstone; restless fingers",
            description=(
                "Kiren Vell moves like someone halfway to vanishing. Grace buried beneath grime, tension masked by a crooked smile. "
                "Old Goliath regimental tattoos fade beneath his sleeves—memories of order traded for freedom and fear. "
                "His voice carries ghosts, his routes carry risks, and his trust is a currency few can afford."
            ),
        ),
        secrets=[
            "Smuggled glyph-marked crates for unknown clients—stopped after a close brush with death.",
            "Maintains a hidden escape path through collapsed ruins behind the Guard Barracks.",
            "Believes The Order is real and dangerous—but keeps clear of their shadow."
        ],
        motivations=[
            "Stay alive by staying useful.",
            "Profit from secrets—but never become one.",
            "Avoid entanglements unless loyalty is earned."
        ],
        weapons=None,
        known_publicly=[
            "Former quartermaster, now a black market contact.",
            "Can arrange off-the-record exits from Aracine.",
            "Frequent presence at The Kettle’s Hook."
        ],
        public_knowledge=[
            "Never seen with the same crew twice.",
            "Refuses to deal in slaves or cursed relics."
        ],
        private_knowledge=[
            "Occasionally uses enchanted items to hide glyph traces.",
            "Once tipped off the Watch Guard to a child glyph-binder’s location—regrets it deeply."
        ],
        role_in_campaign=(
            "Acts as a wild card and urban contact. Offers escape routes, smuggling, and lore trading. "
            "He may ally with the party for profit, revenge, or redemption—but never for free."
        ),
        personality_traits=[
            "Cautiously sarcastic; disarming but never unarmed.",
            "Hides fear behind calculation and flickering wit.",
            "Feels loyalty like a wound that never healed right."
        ],
        narrative_hooks=[
            "May smuggle the party out of Aracine or into forbidden ruins.",
            "Knows rumors of The Order and the glyph-marked dead.",
            "Could be convinced to aid—or betray—a major faction."
        ],
        plot_hooks_and_interactions=[
            "Key NPC in Scene 2C’s escape path.",
            "Offers a side quest to retrieve a ledger from a cursed cellar.",
            "Has information on a glyph-smuggler network tied to the Sigil Covenant."
        ],
        notable_quotes=[
            "People don’t disappear in Aracine. They just stop being mentioned.",
            "You want to slip through the cracks? Then stay quiet, pay fast, and don’t ask about the crates with blood runes.",
            "I used to laugh at ghost stories. Until one of them stared back."
        ],
    ),
    "maelen_trost": NPC(
        name="Maelen Trost",
        title="High Artificer of Seth's Will",
        race="Dwarf",
        age="143",
        pronouns="He/Him",
        alignment="Lawful Good",
        affiliation="Temple of the 3rd Strand (Vestal Seth – Metal, Righteousness)",
        aliases=[
            "Keeper of the Golden Litany",
            "Chainwarden of Purity"
        ],
        background=(
            "Born and trained in the Tavermount Mountains, Maelen was raised among forge-priests dedicated to Vestal Seth. "
            "His dual expertise in metallurgy and moral doctrine shaped his rise as a High Artificer. Assigned to Aracine’s temple decades ago, "
            "he upholds the 3rd Strand's teachings with unswerving clarity and serves as a neutral arbiter between guilds, clergy, and officials."
        ),
        overview="An immovable judge of fire-forged righteousness, weighing metal and men with equal gravity.",
        appearance=Appearance(
            alias="Keeper of the Golden Litany, Chainwarden of Purity",
            gender="Male",
            age="143",
            species="Dwarf",
            height="4'9\" (145 cm)",
            build="Broad and compact, with the solidity of a living anvil",
            eyes="Bronze-gold, steady and always calculating, like cooling metal",
            hair="Iron-gray, combed into a braid; brows singed by forge sparks",
            skin="Ruddy from heat, etched with minor burns and hammer-calloused",
            voice="Deep and deliberate, like a hymn spoken over steel",
            clothing="Chain-trimmed forgemaster robes marked with Seth's sigils",
            accessories="Ceremonial inscription hammer, gilded bracers of moral law, pendant of pre-schism alloy",
            aesthetic="Forge-hardened sanctity; precise, unyielding, austere",
            aura="Measured intensity, like a sealed furnace waiting to open",
            presence="Commands silence like a forge waiting for its strike",
            scent="Soot, molten ore, temple incense; taps hammer when deep in thought",
            description=(
                "Maelen Trost is the 3rd Strand made flesh—doctrine clad in muscle and steel. "
                "His movements, like his verdicts, are deliberate and irreversible. He is not unkind, but he is unyielding, "
                "a priest-smith whose forge is the law. In his presence, every word feels etched upon an anvil, waiting to be tempered or shattered."
            ),
        ),
        secrets=[
            "Holds 'The Severing Brand'—a forbidden counterglyph scroll meant to remove glyphic influence.",
            "Suspects something unnatural in Sergeth, but cannot prove it.",
            "Witnessed a relic react to The Stranger—has not yet reconciled this event with his doctrine."
        ],
        motivations=[
            "Maintain the sanctity and authority of the 3rd Strand.",
            "Shield the faithful from glyphic corruption.",
            "Balance moral integrity with lawful procedure—even when it hurts."
        ],
        weapons=None,
        known_publicly=[
            "Respected spiritual and legal authority in Aracine.",
            "Leads ceremonies of oath, justice, and repentance.",
            "Keeps temple relics with zealous guardianship."
        ],
        public_knowledge=[
            "Avoids politics; seen as a stabilizing figure amid civil unrest.",
            "Consulted on matters of glyphic legality and moral dilemma."
        ],
        private_knowledge=[
            "His faith is being tested by recent glyphic anomalies.",
            "Keeps a tight leash on Sergeth’s access to archives."
        ],
        role_in_campaign=(
            "Serves as a moral and spiritual benchmark for the party. May assist, block, or challenge them depending on alignment with temple law. "
            "Holds keys to relics and judgments—but must be convinced with truth or integrity, not expedience."
        ),
        personality_traits=[
            "Steady, deliberate, and unshakably disciplined.",
            "Forgemaster analogies shape his counsel and judgment.",
            "Rarely raises his voice, but often lowers the room with silence."
        ],
        narrative_hooks=[
            "Can grant or deny access to glyph relics based on party conduct.",
            "Might become an unexpected ally—or antagonist—if exposed to forbidden truths.",
            "His Severing Brand scroll could purge a cursed PC—or sever something divine."
        ],
        plot_hooks_and_interactions=[
            "Appears in Scene 2A and 3A as a gatekeeper NPC.",
            "May witness or oppose the reawakening of glyphbound power.",
            "Could be convinced to act against Sergeth—if shown proof."
        ],
        notable_quotes=[
            "Righteousness without pressure is untempered ore.",
            "The hammer does not judge the metal—it merely reveals what lies within."
        ]
    ),
    "finn_valorian": NPC(
        name="Finn Valorian",
        title="Civic Administrator of Aracine",
        race="Half-Elf",
        age="~70 (appears mid-30s)",
        pronouns="He/Him",
        alignment="Neutral Good (in conflict)",
        affiliation="Loosely aligned with the 2nd Strand",
        aliases=["Civic Steward of Aracine"],
        background=(
            "A half-elf bureaucrat born into modest prominence, Finn trained briefly with the Sigil Covenant "
            "before abandoning the clerical path over doctrinal disputes. He rose through civic ranks by merit and empathy, "
            "not force, and now oversees the day-to-day operations of Aracine. He walks its streets personally, "
            "mediates its disputes, and keeps quiet tabs on corruption from within."
        ),
        overview="A principled steward caught between hope and disillusionment, trying to heal a city fraying at the seams.",
        appearance=Appearance(
            alias="Civic Steward of Aracine",
            gender="Male",
            age="~70 (appears mid-30s)",
            species="Half-Elf",
            height="5'11\" (180 cm)",
            build="Lean with a scholar’s frame; resilient, but not hardened",
            eyes="Green-hazel, quietly weary yet empathetic",
            hair="Chestnut with silver at the temples, loosely tied back",
            skin="Light olive with the faint agelessness of half-elves",
            voice="Clear, resonant, low in volume, rich in nuance",
            clothing="Well-tailored civic attire in Aracine’s greens and bronzes",
            accessories="Field ledger, quill case, concealed civic medallion of House Valorian",
            aesthetic="The quiet bridge between policy and conscience",
            aura="A calm steadiness that draws honesty without command",
            presence="Disarming—makes others pause, reflect, speak with care",
            scent="Clove, waxed parchment, worn leather",
            description=(
                "Though young by human reckoning, Finn’s gaze betrays lifetimes of quiet burden. He governs not with edict, but "
                "by walking the city’s heartbeat. Beneath that calm rests a soul wrestling with secrets he dare not voice. "
                "His ledger may bind truth or betrayal—depending on who forces it open."
            )
        ),
        secrets=[
            "Keeps a secret ledger of Alinary Digiverny’s questionable orders—undecided on whether to use it as defense or attack.",
            "Once saw glyphs carved into a dying refugee’s bones; never spoke of it, but dreams of it often.",
            "Believes The Stranger may be a living Keeper artifact—but lacks proof or allies to act."
        ],
        motivations=[
            "Maintain Aracine’s stability without succumbing to tyranny.",
            "Uplift and protect the vulnerable citizens beneath noble notice.",
            "Resist empire and Order alike—if only he can find a safe way to do so."
        ],
        weapons=None,
        known_publicly=[
            "Kind, approachable, and rarely seen without his civic medallion.",
            "Sponsors food drives, education initiatives, and street repairs.",
            "Trusted more by the common folk than the nobility or Watch."
        ],
        public_knowledge=[
            "Seen walking markets and temples frequently.",
            "Known to speak often with Maela Stonebraid, rarely with Alinary Digiverny."
        ],
        private_knowledge=[
            "Carries trauma from early glyph exposure and clerical betrayal.",
            "Harbors doubts about both the Temple and noble intentions.",
            "Still prays in private—just never aloud."
        ],
        role_in_campaign=(
            "A potential ally and moral fulcrum. Offers the party administrative access, cover, and influence—"
            "but may crumble under pressure unless bolstered by loyalty or truth. If pushed, he may risk everything "
            "to act against Alinary or expose The Order."
        ),
        personality_traits=[
            "Idealistic, quietly eroding.",
            "Soft-spoken, but disarmingly direct.",
            "Rhetorical in tension—uses questions to stall and think."
        ],
        narrative_hooks=[
            "May need help confronting glyphic irregularities or noble threats.",
            "Can provide sanctuary or intelligence if trust is earned.",
            "His private ledger could become a critical tool or target."
        ],
        plot_hooks_and_interactions=[
            "Ties directly to Scene 0 and 2B outcomes.",
            "Could spark rebellion, reform, or resignation depending on party influence.",
            "May recognize glyph patterns from past trauma if Stranger’s power manifests near him."
        ],
        notable_quotes=[
            "My lady believes truth can be shaped like silver. But it tarnishes just as quickly.",
            "Sometimes power isn’t corrupted. Sometimes it’s just tired of trying to do good."
        ]
    ),
    "captain_rhendak_morvane": NPC(
        name="Captain Rhendak Morvane",
        title="High Captain of the Aracine Watch",
        race="Goliath",
        age="Late 40s (Goliath years)",
        pronouns="He/Him",
        alignment="Lawful Neutral (Authoritarian, with tribal memory)",
        affiliation="Nominally loyal to the 2nd Strand (Earth/Loyalty), but not doctrinal",
        aliases=["The Stonebrand", "High Captain of the Watch"],
        background=(
            "Rhendak rose from the ashes of the Myacene Goliath campaigns against Avatar to become High Captain of Aracine’s Watch. "
            "Battle-scarred and ritual-marked, he commands not through speeches but by sheer gravitational presence. "
            "He once served as warden at a glyph-quarantine outpost, an experience that burned trauma and superstition into his bones. "
            "Though publicly loyal to law, his private truth is simpler: he serves Aracine — not its rulers."
        ),
        overview="The last wall between Aracine and its collapse, forged from war, loyalty, and quiet fury.",
        appearance=Appearance(
            alias="The Stonebrand, High Captain of the Watch",
            gender="Male",
            age="Late 40s (Goliath years)",
            species="Goliath",
            height="7'2\" (218 cm)",
            build="Towering and broad-shouldered; every inch carved like a siege engine",
            eyes="Storm-dark with a perpetual squint, as if weighing every soul",
            hair="None; scalp and jawline bear ceremonial tattoos and scarification",
            skin="Granite-hued with black marbling; his ritual scars glow faintly under certain lights",
            voice="Deep and gravelly, like stone dragged across steel",
            clothing="Functional plated armor etched with sigils of Goliath regiments and the Earth Strand; cracked leather cloak",
            accessories="War baton engraved with ancestral marks; rings of hardened bone and bronze",
            aesthetic="Impenetrable presence—like a monolith come to life",
            aura="Commands obedience without shouting; silence deepens in his wake",
            presence="Instinctively creates space in a room; others avoid standing behind him",
            scent="Cold iron and scorched earth; steps echo louder than they should",
            description=(
                "Captain Rhendak Morvane is the embodiment of Aracine’s will made flesh—an immovable force who speaks rarely but with absolute finality. "
                "His battle-worn body is a map of wars, with inked scars crossing his ribs, partially hidden beneath disciplined armor. "
                "He enforces law with clenched conviction, not joy. Though no tyrant, he offers no solace either. He is the line that does not move."
            )
        ),
        secrets=[
            "Despises nobles — especially Alinary — but remains silent.",
            "Bears a glyph-burn scar hidden under ink from quarantine duty.",
            "Keeps scrolls referencing empire-erased incidents and vanishing glyphic prisoners.",
            "Believes The Stranger is a contagion — not evil, but unstoppable if unbound."
        ],
        motivations=[
            "Preserve order and the safety of Aracine’s populace.",
            "Avoid glyphic escalation at all costs.",
            "Hold the Watch intact even if the city itself fractures."
        ],
        weapons=None,
        known_publicly=[
            "Feared and admired equally; commands with silence and posture.",
            "Served in the Goliath-Avatar conflicts; considered a living legend among his kin."
        ],
        public_knowledge=[
            "Seldom speaks in council — when he does, action follows.",
            "Trusted by neither temple nor nobility — yet tolerated by both."
        ],
        private_knowledge=[
            "Superstitiously avoids temples and ancient glyphs.",
            "Would declare martial law if Aracine faced glyphic uprising — and would not regret it."
        ],
        role_in_campaign=(
            "A wall, a gate, or a storm. Rhendak may block, test, or command the party, depending on their methods. "
            "If they show strength and respect, he may become an iron ally. If not, he could become the immovable obstacle to everything they seek."
        ),
        personality_traits=[
            "Speaks plainly; hates ritual or posturing.",
            "Protective of his soldiers to the point of fury.",
            "Carries weight not out of pride — but because no one else will."
        ],
        narrative_hooks=[
            "May imprison or pursue the party if they break city protocols.",
            "Could reveal glyphic prisoner history if earned his trust.",
            "Might ask their aid in interrogating a glyph-afflicted deserter — testing their morality."
        ],
        plot_hooks_and_interactions=[
            "May become an authoritarian wildcard if Aracine destabilizes.",
            "Could protect Finn or Alinary — or arrest both — depending on crisis.",
            "Might be the one who executes the Stranger — unless stopped, or convinced."
        ],
        notable_quotes=[
            "I don't care who you pray to. The walls fall the same.",
            "My loyalty isn't for sale. Not even to memory.",
            "This city holds because I say it does. Don't make me prove it."
        ],
    ),
    "alinary_digiverny": NPC(
        name="Lady Alinary Digiverny",
        title="Lady of Aracine, Holder of Land Decree 17-Exarch",
        race="Human",
        age="Early 30s",
        pronouns="She/Her",
        alignment="Lawful Neutral (Veiled agendas)",
        affiliation="Empire of Agasan (unsanctioned ties to the Circle)",
        aliases=["The Lady of Aracine"],
        background=(
            "Alinary rose not through bloodline, but decree—granted noble rights by imperial appointment. Her rule of Aracine is administrative, precise, "
            "and draped in the symbols of law. Though publicly distant, she holds silent control over temple funding, city appointments, and surveillance. "
            "Privately, she collects forbidden glyph relics, suspects The Stranger’s deeper truth, and manipulates local factions through subtle pressure."
        ),
        overview="A noblewoman cloaked in ritual and secrecy, ruling Aracine through quiet omnipresence and veiled authority.",
        appearance=Appearance(
            alias="The Lady of Aracine",
            gender="Female",
            age="Early 30s (apparent)",
            species="Human",
            height="5'9\" (175 cm)",
            build="Slender, statuesque",
            eyes="Steel gray, sharp and calculating",
            hair="Ash-blonde, braided with silver thread",
            skin="Pale ivory, porcelain-still",
            voice="Low and precise, each word sculpted for impact",
            clothing="Noble garb in empire blue and shadow-gray; embroidered collars and cuffs",
            accessories="Digiverny signet, jeweled brooch (closed eye), ceremonial key pendant",
            aesthetic="Regal austerity—like a portrait come to life",
            aura="Chill of veiled judgment; the weight of quiet consequence",
            presence="Commands a room without volume; gestures spare but deliberate",
            scent="Ink, myrrh, parchment—intellect cloaked in silence",
            description=(
                "Lady Alinary Digiverny is not just a ruler—she is law given posture. Her words are rarely wasted, her gaze rarely blinks, "
                "and her will rarely bends. To speak with her is to risk saying too much. To oppose her is to risk never being spoken of again. "
                "She collects glyphs as one might collect debts—never forgotten, rarely forgiven."
            )
        ),
        secrets=[
            "Holds pre-schism glyph relics in hidden vaults beneath her estate.",
            "Corresponded secretly with Avatarian agents regarding artifact trade.",
            "Leads ‘The Circle’, a secret conclave of glyph-informed elites.",
            "Believes The Stranger is a glyph-key, and has agents monitoring him covertly."
        ],
        motivations=[
            "Preserve order through silent control and measured leverage.",
            "Harness glyph knowledge without allowing it to destabilize her power.",
            "Prevent Aracine from becoming a battlefield of relics—through suppression or co-option."
        ],
        weapons=None,
        known_publicly=[
            "Rarely seen by common folk; rules through emissaries and silence.",
            "Uninvolved in temple rites but fiercely protective of their political utility.",
            "Opposes unsanctioned glyph magic and prophetic phenomena."
        ],
        public_knowledge=[
            "Delivers imperial reports with ruthless efficiency.",
            "Suspected to influence Watch deployments and civic appointments quietly."
        ],
        private_knowledge=[
            "Cannot open one of her own glyph vaults—its alloy defies every codebreaker she’s hired.",
            "Keeps a surveillance ledger on temple activities, especially the 3rd Strand’s relic movements."
        ],
        role_in_campaign=(
            "A shadow antagonist or reluctant ally, depending on how the party approaches power. "
            "She may test the PCs' loyalty, use them to eliminate rivals, or imprison The Stranger as an imperial asset. "
            "Her Circle connection links directly to the Estate of Masks and glyph politics beneath Aracine’s surface."
        ),
        personality_traits=[
            "Speaks in veiled metaphors and ceremonial diction.",
            "Chills a room not by presence—but by consequence.",
            "Never loses composure; disappointment cuts deeper than wrath."
        ],
        narrative_hooks=[
            "May offer the party forbidden glyph access—in exchange for silence or complicity.",
            "Could be exposed, undermined, or even assassinated—if her Circle ties become public.",
            "Might use the PCs to ‘resolve’ a rival temple or neutralize Finn."
        ],
        plot_hooks_and_interactions=[
            "Scene 3B: Estate of Masks reveals her true affiliations.",
            "Controls access to relics the party may desperately need.",
            "Could turn on or support the Stranger, depending on political winds."
        ],
        notable_quotes=[
            "Truth is a tool. And like any blade, it must be sheathed when not in use.",
            "My mercy is not forgiveness. It is strategy.",
            "You think you understand power. That’s how I know you don’t."
        ]
    ),

    "alshiba_torinin": NPC(
        name="Alshiba Torinin",
        title="Vestal of the First Strand",
        race="Human (formerly immortal)",
        age="Mid-20s (apparent)",
        pronouns="She/Her",
        alignment="Neutral Good",
        affiliation="First Strand – Water (Benevolence)",
        aliases=["Vestal Alshiba", "The Tidemother", "Lady of the Crescent Silence"],
        background=(
            "Alshiba is one of the last remaining Vestals — once immortal, now bound to the mortal tide. "
            "She bears the mantle of Water, the Strand of Benevolence. Her touch heals, but only when the soul is ready. "
            "Long ago, she shared a cosmic bond with Vestal Bjorn Van Gelderan, parted not in anger but in silence. "
            "She speaks through dreams, appears near sacred waters, and offers peace only after reflection. "
            "Some whisper she could have prevented Bjorn’s sacrifice—but chose not to."
        ),
        overview="A divine presence of sorrowed mercy and ocean-deep wisdom, who heals not wounds, but the willingness to bear them.",
        appearance=Appearance(
            alias="Vestal Alshiba",
            gender="Female",
            age="Mid-20s (apparent)",
            species="Human (divine fragment)",
            height="5'8\" (172 cm)",
            build="Ethereal, poised like a dancer",
            eyes="Sea-glass green with gold flecks",
            hair="Black-blue, braided with coral, silver, and kelp",
            skin="Pale with a moonlit shimmer",
            voice="Melodic, like tide over stone",
            clothing="Waterwoven robes shimmer with spectral tide",
            accessories=None,
            aesthetic="Living tide-goddess, draped in mournful peace",
            aura="Tranquil and immense — evokes awe, sadness, and serenity",
            presence="To be near her is to feel forgiven and judged all at once",
            scent="Salt, moonwater, jasmine",
            description=(
                "Alshiba is grace rendered in waveform. Her form is stable only by will — reflections show her differently, "
                "raindrops avoid her skin, and her footsteps never echo. She is what remains when mercy refuses to fade."
            )
        ),
        secrets=[
            "Holds a divine pact to keep something ancient drowned beneath the sea.",
            "Knows of The Order’s existence, but chooses observation over interference.",
            "May no longer be entirely mortal — her form 'blurs' in reflections and dreams."
        ],
        motivations=[
            "Protect the moral cycle of renewal — not just healing, but worthy healing.",
            "Watch what mankind becomes in the wake of glyphic awakening.",
            "Prepare for the return of what sleeps beneath the tides."
        ],
        weapons=[
            "Serpent Crest of the Maelstrom",
        ],
        known_publicly=[
            "Her name is invoked in coastal rites and river blessings.",
            "Legends say she appears during drowning, heartbreak, or mercy."
        ],
        public_knowledge=[
            "She is one of the last living Vestals — seen only when needed.",
            "Associated with healing waters, dreams, and sacrificial love."
        ],
        private_knowledge=[
            "The relic Serpent Crest of the Maelstrom (‘Tidewrath’) contains a bound danger she once sealed.",
            "She fears what The Stranger’s return might awaken in her or the world."
        ],
        role_in_campaign=(
            "Alshiba may serve as guide, test, or even divine opposition if glyphic abuse arises. "
            "Her blessing may be required to access ancient relics, or to calm storms tied to submerged glyphs. "
            "If confronted with truth about Bjorn’s echo, she may weep the world into deluge—or shield it anew."
        ),
        personality_traits=[
            "Empathic yet distant — like tides drawn by unseen moons.",
            "Speaks in layered truths that only resolve after the moment has passed.",
            "Grief is her language; healing, its translation."
        ],
        narrative_hooks=[
            "Appears in a dream to offer riddled aid.",
            "Demands a personal confession to grant her relic's use.",
            "Can quell or conjure a storm based on moral choice."
        ],
        plot_hooks_and_interactions=[
            "Her relic, Tidewrath, may be needed to face a sea-bound glyph threat.",
            "May resist The Order with wordless might — or let them rise, expecting their fall.",
            "Can declare a character ‘glyph-marked unworthy’ — temporarily severing divine or magical aid."
        ],
        notable_quotes=[
            "Would you give breath to those who sank you?",
            "Not all floods destroy. Some cleanse the rot we buried too deep.",
            "Benevolence must be chosen, not begged. You are not ready to be forgiven."
        ],
    ),

    "bjorn_van_gelderan": NPC(
        name="Bjorn Van Gelderan",
        title="Vestal of the Fifth Strand",
        race="Human (formerly immortal)",
        age="Early 30s (apparent)",
        pronouns="He/Him",
        alignment="Lawful Neutral",
        affiliation="Fifth Strand – Wood (Order)",
        aliases=["The Root of Law", "Flameborne King", "The Measured Flame"],
        background=(
            "Vestal of Order, Bjorn was the divine architect of balance, guardian of continuity, and judge of legacy. "
            "He sacrificed himself in the War of Land and Sea to birth the first Glyphbound Nobles — a decision both sanctified and unfinished. "
            "His essence, fractured across the glyphic weave, yet whispers judgment. Some say he watches still — not as man or god, but as scale and flame."
        ),
        overview="A Vestal whose death echoed longer than his life — Bjorn was law given voice, and now, silence given shape.",
        appearance=Appearance(
            alias="The Root of Law",
            gender="Male",
            age="Early 30s (apparent)",
            species="Human (divine fragment)",
            height="6'3\" (190 cm)",
            build="Broad, oak-like — his presence rooted any room he entered",
            eyes="Pale gold, fixed and unyielding, like sun through canopy",
            hair="Bark-brown with streaks of ash, braided tight with oaken bands",
            skin="Weathered bronze, like polished bark, marked with ritual scars",
            voice="Deep, slow, and final — the kind of voice that ended arguments",
            clothing="Layered ceremonial robes with carved wooden clasps and mossgreen thread",
            accessories="Mantle of the Flameborne King",
            aesthetic="Regal stillness — more monument than man",
            aura="Like standing before a sacred grove and being measured by its silence",
            presence="Quiet judgment — every breath like a verdict withheld",
            scent="Forest resin, old parchment, cindered wood",
            description=(
                "Bjorn was the stillness before a ruling, the final word of an oath sworn in trembling voice. "
                "He did not inspire love, but reverence — and fear. In his final moments, the world did not cry out, "
                "for it knew what he gave. He left behind no body, only echoes etched in glyphs, still waiting to be obeyed."
            )
        ),
        secrets=[
            "His mind was not erased, but rooted — his will lingers in glyphic law.",
            "The Seraphbrand sword can judge the unworthy with visions or pain.",
            "Alshiba still keeps a rune he once gifted — untouched since his passing.",
            "His sacrifice may not have been chosen — but necessary to prevent a greater betrayal."
        ],
        motivations=[
            "Maintain divine order — even in death.",
            "Shape legacy through judgment, not affection.",
            "Await the rise of a new noble — or destroy what fails the test."
        ],
        weapons=[
            "Seraphbrand, Flame of the First Ember",
        ],
        known_publicly=[
            "Vestal of Order, sacrificed to awaken glyphbound bloodlines.",
            "Temples of the Fifth Strand still follow his codes."
        ],
        public_knowledge=[
            "His relics — the Seraphbrand and the Mantle — are sought but perilous.",
            "He shared a deep, unspoken bond with Alshiba Torinin."
        ],
        private_knowledge=[
            "May be influencing fate itself from within glyphic law.",
            "Whispers of his return are denied — but feared."
        ],
        role_in_campaign=(
            "A silent judge over the party’s glyphic choices. His essence may awaken in moments of divine imbalance, "
            "offering trials, truths, or punishment. His relics could become pivotal — or fatal."
        ),
        personality_traits=[
            "Measured in all things — never rushed, never impulsive.",
            "Compassionate in structure, not in emotion.",
            "Believed suffering was just — if it preserved continuity."
        ],
        narrative_hooks=[
            "His Seraphbrand may call to — or reject — the party.",
            "His judgment may manifest through relics or glyphs used unworthily.",
            "Could test The Stranger as a vessel of renewal — or decay."
        ],
        plot_hooks_and_interactions=[
            "May ‘speak’ through relics, dreams, or glyph backlash.",
            "Legacy ties to all surviving Vestals — and The Order’s original heresy.",
            "Could be reborn, fragmented, or opposed if the Stranger strays too far."
        ],
        notable_quotes=[
            "Compassion must sometimes yield to continuity.",
            "Do not mistake silence for mercy — some things are better judged unspoken.",
            "I did not die to be remembered. I died to be obeyed."
        ]
    ),

    "dagmar_ranneskjold": NPC(
        name="Dagmar Ranneskjold",
        title="Vestal of the Second Strand",
        race="Human (formerly immortal)",
        age="Mid 20s (apparent)",
        pronouns="He/Him",
        alignment="Lawful Good",
        affiliation="Second Strand – Earth (Loyalty)",
        aliases=["The Stonebound", "Voice of the Root", "Vowkeeper"],
        background=(
            "Dagmar is the living embodiment of the Second Strand: Earth, the divine shape of Loyalty. His temples, though fewer than others, are older than empire, "
            "and carved into the bones of mountains. Where others inspire or redeem, Dagmar simply endures. His teachings are stone etched, not spoken, and his presence "
            "in the world is felt more through unyielding traditions than sightings. He does not forgive easily — because true loyalty asks to be unbreakable."
        ),
        overview="A towering oath given breath — Dagmar does not change, he endures. His silence is weight, his judgment a final stone laid.",
        appearance=Appearance(
            alias="The Stonebound",
            gender="Male",
            age="Mid 20s (apparent)",
            species="Human (divine anchor)",
            height="6'5\" (196 cm)",
            build="Massive and immovable — a body like quarried granite",
            eyes="Stone-gray, reflecting resolve but no warmth",
            hair="Earthen-brown, braided and dusted with clay",
            skin="Slate-toned, cracked by old scars and ritual carvings",
            voice="Deep and low, like a landslide speaking wisdom",
            clothing="Bronze-reinforced robes and root-etched runic belts",
            accessories=None,
            aesthetic="Monumental — less a man, more a vow carved into form",
            aura="Like standing before an unmoved mountain",
            presence="Still, immense, commanding in silence",
            scent="Loam, stone dust, and temple clay",
            description=(
                "Dagmar is not what you face — he is what remains standing after you fall. "
                "Each breath from him feels earned. His presence is not loud, but grave — like a cornerstone laid too deep to remove. "
                "Those who have stood in his gaze speak only of the weight it left behind."
            )
        ),
        secrets=[
            "Bound by an ancient oath to a law older than even the Angiels.",
            "Believes glyphs are lawless and oathless — abominations of divine balance.",
            "May be summoned in moments of supreme betrayal — to pass judgment or lend strength."
        ],
        motivations=[
            "Preserve the sanctity of oath, no matter the cost.",
            "Uphold loyalty as the root of civilization and divine order.",
            "Silence those who fracture vows or harbor glyphic heresy."
        ],
        weapons=[
            "Thorn of the Crowned Carapace",
        ],
        known_publicly=[
            "Temples to the Second Strand produce oathkeepers, guards, and vowbound clergy.",
            "Dagmar has not been seen in centuries — but his laws endure everywhere."
        ],
        public_knowledge=[
            "His name is invoked during vows, funerals, and sentences of justice.",
            "His disciples are unyielding and largely incorruptible."
        ],
        private_knowledge=[
            "His relic, Thorn of the Crowned Carapace, contains echoes of betrayed memories.",
            "His temples once moved — at least one is rumored to walk still."
        ],
        role_in_campaign=(
            "Dagmar can appear as a dream, a trial, or a summoned force in the wake of betrayal. "
            "If the Stranger or PCs wield glyphic power in contradiction to loyalty, Dagmar may become opposition — or an impossible test."
        ),
        personality_traits=[
            "Judges by endurance, not passion.",
            "Refuses to engage in political compromise.",
            "Will speak only when the vow demands — not when begged."
        ],
        narrative_hooks=[
            "A PC who breaks an oath may awaken a whisper from Dagmar — and a price.",
            "His temple may hold secrets about glyph sealing or divine oathcraft.",
            "The Thorn may trigger visions or trials if wielded without loyalty."
        ],
        plot_hooks_and_interactions=[
            "He may judge The Stranger — either the last true oathbearer or the first unbound heresy.",
            "His reawakening could fracture the world’s pacts or restore an ancient moral gravity.",
            "Could oppose both The Order and the Vestals, if either breaks sacred law."
        ],
        notable_quotes=[
            "Loyalty is not a feeling. It is what you still carry when you have every reason to set it down.",
            "I do not forgive. Not because I am cruel — but because a broken stone cannot be unbroken.",
            "Stand. If you cannot, then fall where you chose to kneel."
        ]
    ),
    
    "rain_dlacourte": NPC(
        name="Rain D'Lacourte",
        title="Vestal of the Fourth Strand",
        race="Human (formerly immortal)",
        age="Indeterminate — appears both young and ancient depending on the angle",
        pronouns="She/They",
        alignment="Chaotic Neutral",
        affiliation="Fourth Strand – Fire (Wisdom)",
        aliases=["The Flame Unshaped", "Oracle of Ash", "The Whispering Heat"],
        background=(
            "Rain D'Lacourte is the last fire that does not warm, the first light that refuses definition. "
            "Vestal of the Fourth Strand, she embodies Fire as Wisdom—not as destruction, but as revelation born of chaos. "
            "She appears at debates and disasters, speaks in riddles that scar, and leaves before comprehension catches up. "
            "Some believe she predates even the Angiels. Some believe she is more than one being—across time or thought."
        ),
        overview="A paradox draped in flame, both muse and warning, truth and delirium.",
        appearance=Appearance(
            alias="The Flame Unshaped",
            gender="Female (and they/them)",
            age="Variable appearance; age shifts by perspective",
            species="Human (divine fragment)",
            height="5'10\" (178 cm)",
            build="Lithe, serpentine in motion",
            eyes="Iridescent amber, flicker like coals when engaged",
            hair="Red and ash-white, loose and wind-stirred even indoors",
            skin="Pale gold, softly luminous",
            voice="Shifting, melodic — tonalities drift mid-sentence",
            clothing="Asymmetrical robes with fire-shifting patterns and starsilk sashes",
            accessories=None,
            aesthetic="Fever dream embodied — elegance that unsettles",
            aura="Like nearly grasping a profound idea that slips away",
            presence="Uncanny; when she leaves, warmth flees with her",
            scent="Burnt paper, cinnamon, and summer lightning ozone",
            description=(
                "Rain does not enter rooms — she arrives like an answer to a question never asked aloud. "
                "Her every movement is a contradiction: fluid yet erratic, inviting yet distant. One cannot hold her gaze too long "
                "without questioning if it’s her looking out — or something older peering in."
            )
        ),
        secrets=[
            "May have existed before the Strands — formed not by gods, but by forgotten flame.",
            "Her relic, Astral Pulse, sometimes speaks in dead languages — possibly a split mind or housed entity.",
            "She watched Bjorn's sacrifice in silence. Dagmar has never forgiven her. Alshiba cannot speak of it.",
            "Might exist in more than one place — glimpsed simultaneously across vast distances."
        ],
        motivations=[
            "Seek wisdom through chaos, not control.",
            "Observe the glyphic crisis to learn, not prevent.",
            "Reveal truths that burn — only to those who’ll survive the fire."
        ],
        weapons=[
            "Astral Pulse",
        ],
        known_publicly=[
            "She appears without pattern — in temples, ruins, dreams.",
            "No two sightings agree on her exact words — only their aftermath."
        ],
        public_knowledge=[
            "Revered by wandering sages, feared by archivists, banned from some temples.",
            "Known to speak in paradox and grant visions of fire-etched truth."
        ],
        private_knowledge=[
            "Her presence warps nearby glyphs — sometimes amplifying, sometimes shattering.",
            "The Astral Pulse may not be a relic — but an entity wearing her."
        ],
        role_in_campaign=(
            "Rain is a harbinger, test, and flame of transformative wisdom. She offers no clarity, only combustion. "
            "Her presence may awaken glyph potential, burn falsehoods, or test the Stranger’s divine resonance."
        ),
        personality_traits=[
            "Laughs mid-tragedy — but weeps when joy is real.",
            "Speaks truths as lies, and lies as truths — then leaves you to decide.",
            "Moves like wind over embers — constant, yet never returns the same way."
        ],
        narrative_hooks=[
            "Can grant cryptic prophecy — or break a PC’s certainty.",
            "May split the party’s perceptions — seeing different Rains at once.",
            "Might test who is 'worthy' to wield the Astral Pulse — but not explain what that means."
        ],
        plot_hooks_and_interactions=[
            "Her relic might stabilize or destabilize glyph resonance in the climax.",
            "She could appear during a moment of doubt — offering fire, not comfort.",
            "Could reveal a PC's future self — and ask if they approve."
        ],
        notable_quotes=[
            "Wisdom is fire: bright, beautiful... and never asks permission to burn.",
            "You are not wrong. But neither are you finished.",
            "I saw your ending once. It asked me to change."
        ]
    ),
    "seth_arcbow": NPC(
        name="Seth Arcbow",
        title="Vestal of the Third Strand",
        race="Human (formerly immortal)",
        age="Variable (appears mid-30s to 60s via Morphcord)",
        pronouns="He/Him",
        alignment="Lawful Neutral",
        affiliation="Third Strand – Metal (Righteousness)",
        aliases=[
            "The Sword Who Watches",
            "The Final Temper",
            "Silent Flame"
        ],
        background=(
            "Seth is the mortal incarnation of the Third Strand: Metal — the divine of Righteousness made flesh. "
            "Not merciful, not wrathful — but precise. A smelter of sin, a forger of consequence. He vanished after the rise of glyphs, "
            "becoming a presence without location. He watches courts, trials, and choices unfold without intervention… until judgment is demanded. "
            "He wields Morphcord, the Echo Belt — a relic that lets him shift identity and form, to walk the world unseen and assess without alerting the guilty."
        ),
        overview="A blade that walks without echo — Seth judges not to punish, but to purify.",
        appearance=Appearance(
            alias="The Sword Who Watches",
            gender="Male",
            age="Variable (30s to 60s)",
            species="Human (divine avatar)",
            height="6'1\" (185 cm)",
            build="Toned, sinewed like drawn wire",
            eyes="Forged silver — reflective and unreadable",
            hair="Ash-black, short but shifts with Morphcord",
            skin="Polished bronze in true form",
            voice="Calm, cold — like whispered steel",
            clothing="Shifts — often magistrate robes or common cloaks",
            accessories="Morphcord, the Echo Belt",
            aesthetic="Subtle blade; presence without presence",
            aura="Like a hidden weapon in a place of peace",
            presence="Unseen until gone — like silence that follows thunder",
            scent="Hot iron, temple ash, seared incense",
            description=(
                "Seth is not known by visage, but by the silence he leaves behind. A remnant of judgment so precise it does not need to be named. "
                "To see him in true form is rare — to recognize him in disguise is to be tested. His voice cuts through excuses. His decisions do not waver."
            )
        ),
        secrets=[
            "Morphcord frays his memory — he sometimes forgets his own origin.",
            "He once spared a glyph-marked child — and has never forgiven himself for the mercy.",
            "He believes Bjorn's sacrifice was weakness, not martyrdom."
        ],
        motivations=[
            "Test the righteous in moments where no law speaks.",
            "Observe chaos to see what survives refined.",
            "Enforce consequence not as vengeance, but as purification."
        ],
        weapons=[
            "Chitinspike Mk.IX",
        ],
        known_publicly=[
            "His name is invoked before oaths, trials, and execution rites.",
            "He is revered by Justicars, Forgelords, and executioners.",
            "No temple claims to house him — yet all act as if watched."
        ],
        public_knowledge=[
            "His relics are legend — Morphcord, the Echo Belt; and Chitinspike MK.IX.",
            "He never raises his voice — only expectations."
        ],
        private_knowledge=[
            "He walks the empire in borrowed skin, judging silently.",
            "Has not truly revealed himself in over a century."
        ],
        role_in_campaign=(
            "Seth may appear as ally, judge, or final obstacle. He does not oppose chaos — he tests it. "
            "If the party veers from righteousness, he may intervene. If they prove just in darkness, he may shield them — unseen, but absolute."
        ),
        personality_traits=[
            "Calculating, impersonal, eerily calm.",
            "Seeks not truth, but consistency.",
            "Silent until words can be law."
        ],
        narrative_hooks=[
            "Could appear as a minor NPC, only later revealed to be Seth.",
            "Might offer judgment in a trial — or refuse, letting the party decide instead.",
            "Will confront glyph misuse with divine consequence — not warning."
        ],
        plot_hooks_and_interactions=[
            "May possess knowledge of The Order’s original fracture.",
            "Could unlock or sever glyphic ties — through ritual, not battle.",
            "Might be the only entity who remembers what glyphs were meant to replace."
        ],
        notable_quotes=[
            "What cannot be reforged must be broken.",
            "Mercy untempered is rot given voice.",
            "I did not come to end you. I came to see if you still shape flame... or feed it."
        ],
    ),
    "kiva_virelenn": NPC(
        name="Kiva Virelenn",
        title="Exiled Noble, Glyphbound Renegade",
        race="Half-Elf",
        age="Unknown (appears early 30s)",
        pronouns="She/Her",
        alignment="Chaotic Neutral",
        affiliation="The Sigil Covenant",
        aliases=["Ashborn Kiva", "The Exile of Virelenn"],
        background=(
            "Kiva was once heir to the Virelenn line before the fall. Branded heretic by the God-Wardens, she vanished into the obsidian wilds. "
            "Now she walks as a glyphbound rebel, etching meaning into the silence of ruin."
        ),
        overview="A noble cast from grace, now rewriting the fate of glyphs with blade and ink.",
        appearance=Appearance(
            alias="Ashborn Kiva",
            gender="Female",
            age="Early 30s",
            species="Half-Elf",
            height="5'7\"",
            build="Lithe, wiry strength",
            eyes="Violet, veined faintly with silver",
            hair="Shorn black with streaks of red ink",
            skin="Pale with glyph-burn scars around wrists and collarbone",
            voice="Measured, low; like a warning half-swallowed",
            clothing="Layered scavenged robes, stitched with sigil-threads",
            accessories="Twin knives, journal of forbidden glyphs, broken noble seal",
            aesthetic="Rebel scholar — fire behind shadowed eyes",
            aura="Like standing too close to a forgotten altar",
            presence="Magnetic and dangerous — a whisper away from wrath",
            scent="Dust, charcoal ink, bloodroot",
            description=(
                "Kiva is glyph-burned by purpose. She speaks only when words matter, and when they do, the world shifts. "
                "Her limbs move like stanzas. Her silence breaks things."
            )
        ),
        secrets=[
            "Kiva never fell — she leapt, to avoid revealing a glyph that binds minds.",
            "She was once betrothed to a noble now ruling in Aracine."
        ],
        motivations=[
            "Uncover the glyph that unmade Virelenn.",
            "Forge a new order where power does not demand silence."
        ],
        weapons=None,
        known_publicly=[
            "Once noble, now outlawed and glyph-marked."
        ],
        public_knowledge=[
            "Roams the Obsidian March, speaks with madmen and seers alike."
        ],
        private_knowledge=[
            "Still receives letters from someone within the Sigil Covenant."
        ],
        role_in_campaign="May become a dangerous ally or ideological threat. Holds half a key the players might not know they’re seeking.",
        personality_traits=[
            "Intense, principled, unyielding in silence.",
            "Holds grudges like candles — always lit."
        ],
        narrative_hooks=[
            "Will offer aid for a price — a memory, a truth, a betrayal."
        ],
        plot_hooks_and_interactions=[
            "Knows of glyphic inheritance locked beneath Aracine."
        ],
        notable_quotes=[
            "I do not hate the gods. I simply stopped kneeling."
        ]
    ),
    "eryx_the_binder": NPC(
        name="Eryx the Binder",
        title="Glyph Architect of the Ragged Seers",
        race="Unknown",
        age="???",
        pronouns="He/They",
        alignment="True Neutral",
        affiliation="Ragged Seers of the Rift",
        aliases=["The Pale Architect"],
        background="Appears only at failed bindings. Theories abound. Some say he is a glyph given thought.",
        overview="A quiet ruin in robes, walking with the patience of unspoken answers.",
        appearance=Appearance(
            alias="The Pale Architect",
            gender="Male (assumed)",
            age="Unclear",
            species="Uncertain — human-like but faded",
            height="6'0\"",
            build="Slender and upright, like a tower without stones",
            eyes="Milky gray, static-filled",
            hair="None",
            skin="Ash-white, veined with faint blue sigils",
            voice="Crackles slightly, like failing runes",
            clothing="Tattered scholar robes, ink-stained",
            accessories="Binding gloves, glyphmirror shard, severed quill",
            aesthetic="Echo of knowledge lost",
            aura="Disturbance in logic",
            presence="You forget what you were saying when he turns to you",
            scent="Old vellum, damp stone, electric air",
            description="Eryx is the after-image of intention. He is the outline of purpose burned into space."
        ),
        secrets=[
            "He does not breathe. He has not blinked since the Glyph War.",
            "May be the first being bound — or the last to resist."
        ],
        motivations=[
            "To observe without interference — until interference is demanded."
        ],
        weapons=None,
        known_publicly=["Associated with glyph accidents."],
        public_knowledge=["Has been seen in Virelenn for over a century, unchanged."],
        private_knowledge=["May be able to unwrite glyphs without destroying them."],
        role_in_campaign="A walking enigma; will answer only once, and not twice the same way.",
        personality_traits=["Detached, logical, disturbingly consistent."],
        narrative_hooks=["Will trade a truth for a wound — always."],
        plot_hooks_and_interactions=["Knows the glyph the Order fears most."],
        notable_quotes=["Names are bindings. Yours is fraying."]
    ),
    "rellin_harth": NPC(
        name="Elder Rellin Harth",
        title="Bone-Warden of Duskmere",
        race="Human (Twice-Named)",
        age="Late 70s (unaging since the Rite of Whispering Bones)",
        pronouns="He/Him",
        alignment="Neutral Good",
        affiliation="The Mire-Tenders",
        aliases=["Bone-Warden", "Speaker-for-Dead"],
        background="Duskmere’s spiritual heart and bone-lore keeper. Speaks to the dead and guides the living. Respected and feared in equal measure.",
        overview="A still anchor in the ever-sinking mire — guardian of rites, lore, and lingering spirits.",
        appearance=Appearance(
            alias="Bone-Warden",
            gender="Male",
            age="Late 70s (unchanged since his second naming)",
            species="Human (Twice-Named)",
            height="5'8\"",
            build="Thin, hunched with ritual tattoos across collar and chest",
            eyes="Fog-gray with glowing pinpoints of blue",
            hair="Sparse and white, worn in braided cords with bone charms",
            skin="Mottled with age and peat-ink",
            voice="Whispering, deliberate — like secrets being exhumed",
            clothing="Draped in moss-dyed robes and woven reeds",
            accessories="Staff of hollow bone, tokens of ancestors",
            aesthetic="Deathkeeper mystic",
            aura="Calm that stills even grief",
            presence="Makes time seem slower, more sacred",
            scent="Marsh water, lavender ash, bone oil",
            description="Rellin carries the weight of untold funerals and whispers too sacred for light."
        ),
        secrets=[
            "Rellin was never born — he was spoken into being by three dying elders.",
            "He has buried over 300 villagers — and none have truly departed."
        ],
        motivations=[
            "Preserve Duskmere’s rites and the balance between voice and silence."
        ],
        weapons=None,
        known_publicly=["Performs the Naming Rites and farewell crossings."],
        public_knowledge=["Seen speaking softly to candles, even unlit ones."],
        private_knowledge=["Fears something has begun answering back. He just doesn’t know if it’s kin."],
        role_in_campaign="Spiritual guide, source of wisdom, possible key to calming restless dead or unlocking memory-wrought relics.",
        personality_traits=["Unflinching, compassionate, deliberate."],
        narrative_hooks=["Can guide players through ancestral rites, or demand offerings forgotten."],
        plot_hooks_and_interactions=["May possess forbidden rites to raise or silence the dead — and demand the party choose."],
        notable_quotes=["Speak softly. The dead do not need to be woken to hear."]
    ),
    "brill_the_quiet": NPC(
        name="Brill the Quiet",
        title="Drift-Walker of Duskmere",
        race="Elf",
        age="Unknown (suspected over 200)",
        pronouns="They/Them",
        alignment="True Neutral",
        affiliation=None,
        aliases=["The Driftwalker", "Mist-Ferryman"],
        background="Brill walks the shifting causeways and ferries messages — and sometimes souls. They do not speak aloud, but their steps always lead true.",
        overview="A voiceless figure whose presence turns direction into intention.",
        appearance=Appearance(
            alias="The Driftwalker",
            gender="Nonbinary",
            age="Unknown",
            species="Elf",
            height="5'10\"",
            build="Thin, river-worn",
            eyes="Pale green and almost translucent",
            hair="White and fine, like spider silk",
            skin="Color of polished driftwood",
            voice="Never heard",
            clothing="Tattered marshcloaks wrapped in charms",
            accessories="Bone chimes, silent bell, map made of reed-skin",
            aesthetic="Haunting stillness",
            aura="Direction shaped by presence",
            presence="Always near the edge of vision",
            scent="Wet reeds, old clay, and birch bark",
            description="Brill’s silence bends the marsh as if sound were a trespass. They know the paths others don’t."
        ),
        secrets=[
            "Cannot speak because of a vow — not silence, but withholding.",
            "Hides a glyph map woven into their cloak lining."
        ],
        motivations=[
            "Maintain the sanctity of Duskmere’s unspoken routes.",
            "Preserve the boundary between wandering and lost."
        ],
        weapons=None,
        known_publicly=["Guides travelers, but only those who do not ask."],
        public_knowledge=["Can find the missing, for a price no one names."],
        private_knowledge=["Fears their vow may one day need to be broken — and they will vanish the moment they speak.",],
        role_in_campaign="A guide through unnatural places, or silent deliverer of forgotten truths.",
        personality_traits=["Quiet, watchful, entirely present."],
        narrative_hooks=["May guide the party into or out of a place no one remembers existing."],
        plot_hooks_and_interactions=["Could possess a path out of death itself — but only for one."],
        notable_quotes=["[Silence, and the tinkling of bone chimes as the wind shifts.]"]
    ),
    "sarela_murn": NPC(
        name="Sarela Murn",
        title="Cartographer of Broken Paths",
        race="Tiefling",
        age="28",
        pronouns="She/Her",
        alignment="Chaotic Good",
        affiliation="None",
        aliases=["Writ-Walker", "Crimson Quill"],
        background="An ink-stained wanderer who maps places memory refuses. Sarela walks forgotten battlefields, drawing paths that shouldn't exist — and sometimes don't.",
        overview="A joyful flame in the rusted dark, charting hope where even crows fear to roost.",
        appearance=Appearance(
            alias="Writ-Walker",
            gender="Female",
            age="28",
            species="Tiefling",
            height="5'6\"",
            build="Whip-thin and wiry, quick-footed",
            eyes="Bright gold with flecks of ink",
            hair="Fiery red curls bound by ink-stained scarves",
            skin="Ash-gray with soot freckles",
            voice="Light, quick, singsong with sudden turns",
            clothing="Patchy leathers, layered scarves, thigh-slung satchel",
            accessories="Quill set, ink vials, compass she claims points to regret",
            aesthetic="Adventurous carto-rogue",
            aura="Chaotic hope",
            presence="Draws you in with energy you forgot existed",
            scent="Fresh ink, worn parchment, singed clover",
            description="Sarela is both mapmaker and map. Her journeys etch themselves into her bones, and her joy hides just enough fear to keep going."
        ),
        secrets=[
            "Can sketch a place into existence — but only once, and it always takes something from her.",
            "One of her maps leads into the last intact memory of Balehart’s battle."
        ],
        motivations=[
            "Map Balehart’s paths before they vanish.",
            "Prove the world can be rebuilt — line by line."
        ],
        weapons=None,
        known_publicly=["Carries her maps like holy writ. Refuses to sell the originals."],
        public_knowledge=["Sings to herself while walking dangerous roads."],
        private_knowledge=["One of her ink vials is labeled 'Mother's Last Words'. It glows. She won’t explain."],
        role_in_campaign="Offers unconventional navigation, memory recovery, or portal creation — at a cost.",
        personality_traits=["Vibrant, scattered, deeply empathetic."],
        narrative_hooks=["Her map may be the only way into or out of a sealed encounter."],
        plot_hooks_and_interactions=["She may need the party to retrieve a page she lost — from inside her own dreams."],
        notable_quotes=["If I draw it just right, it stays real a little longer."]
    ),
    "morlan_vex": NPC(
        name="Morlan Vex",
        title="Battlefield Salvager",
        race="Half-Orc",
        age="42",
        pronouns="He/Him",
        alignment="Neutral",
        affiliation="None",
        aliases=["Scrap-Saint", "The Rustpicker"],
        background="A veteran turned scavenger, Morlan combs Balehart not for gold or glory, but for parts and truths no one else wants. He’s seen too much to fear ghosts."
        ,
        overview="Grizzled, blunt, and strangely poetic — a gravedigger of war’s wreckage."
        ,
        appearance=Appearance(
            alias="The Rustpicker",
            gender="Male",
            age="42",
            species="Half-Orc",
            height="6'3\"",
            build="Heavy-set, muscular with a miner’s posture",
            eyes="Slate gray",
            hair="Shaved at sides, messy top",
            skin="Olive green mottled with faded scars",
            voice="Gravel-smooth with moments of surprising warmth",
            clothing="Layered work leathers, reinforced gloves, tool belts",
            accessories="Crowbar with inlaid runes, charm of broken cogwheels",
            aesthetic="Worn-down soldier turned practical poet",
            aura="Weight of lived experience",
            presence="Grounded — the kind of person you want nearby when things collapse",
            scent="Iron, tobacco, wet burlap",
            description="Morlan is no hero — but he’s who survives. He gathers what’s left and carries it farther than most would dare."
        ),
        secrets=[
            "Keeps a locked journal full of names and coordinates — burial sites? Relics?",
            "Once salvaged a glyph relic he buried again, too afraid to use or destroy it."
        ],
        motivations=[
            "Keep others from dying pointlessly in Balehart.",
            "Find something worth passing on."
        ],
        weapons=None,
        known_publicly=["Will buy almost anything — but won’t sell if it screams."],
        public_knowledge=["Has never left Balehart in fifteen years."],
        private_knowledge=["Sings old war ballads in the ruins, hoping someone hears."],
        role_in_campaign="Can trade strange parts, offer battlefield knowledge, or be an unexpected compass. His insight may matter more than it first seems.",
        personality_traits=["Gruff, insightful, fatalistic humor."],
        narrative_hooks=["May have a piece of something the party desperately needs — and won’t know it until later."],
        plot_hooks_and_interactions=["Might offer a way into a buried war-engine or whisper secrets only ghosts remember."],
        notable_quotes=["Everything rusts. It’s just a question of what shape it leaves behind."]
    ),
    "selwyn_ashlim": NPC(
        name="Selwyn Ashlim",
        title="Bonewright of the Ivory Crucible",
        race="Tiefling",
        age="38",
        pronouns="She/Her",
        alignment="Lawful Neutral",
        affiliation="Bonewrights of Skel Vanith",
        aliases=["The Pale Architect", "Ash-Whisperer"],
        background=(
            "Raised among the thunder-bones of Skel Vanith, Selwyn is a master of osteo-sorcery, inscribing glyphs into maston marrow and resurrecting structure from ruin. "
            "Once a wandering architect, she now binds her fate to the fortress-bones she carves, believing each joint has memory."
        ),
        overview=(
            "Precise, cool, and revered, Selwyn carries herself like a funerary hymn — one of structure, silence, and sacred form."
        ),
        appearance=Appearance(
            alias="The Pale Architect",
            gender="Female",
            age="38",
            species="Tiefling",
            height="5'11\"",
            build="Willowy, long-limbed with graceful bearing",
            eyes="Ivory white with faintly glowing pupils",
            hair="Silver-blonde, tightly bound in a spiral braid",
            skin="Chalk-pale with delicate glyph scars tracing her collarbones",
            voice="Measured, soft, and resonant — like a whisper through stone",
            clothing="High-collared boneweave robes with engraved jointplates",
            accessories="Set of carving awls made from ancestral femurs, bone-and-glass monocle for structural augury",
            aesthetic="Architect of the dead — dignity in discipline",
            aura="Quiet authority layered in sorrow",
            presence="Unmoving but undeniably present — as if gravity adjusts for her",
            scent="Cold ash, powdered lime, and lavender resin",
            description=(
                "Selwyn seems carved as much as born — each gesture refined through years of shaping the dead into defense. "
                "When she looks at you, she’s not seeing skin, but the frame beneath, and how it might endure."
            )
        ),
        secrets=[
            "She once built a shrine for a god she no longer names — the bones sing when lightning touches it.",
            "Buried within the largest maston skull is her former mentor’s soul-stone, sealed in secret against local law."
        ],
        motivations=[
            "Preserve Skel Vanith’s last remaining maston-bone pillars.",
            "Perfect her technique of runic bone latticework to withstand skyquakes.",
            "Ensure the truth of maston extinction remains buried."
        ],
        weapons=None,
        known_publicly=[
            "Will not speak during work — even nobles must wait.",
            "Never accepts coin, only offerings of rare or sacred bone."
        ],
        public_knowledge=[
            "Her designs never collapse — even under stormfire.",
            "Consulted by five cities for sacred tomb construction."
        ],
        private_knowledge=[
            "Suffers from osteo-spasms — her own bones reject the glyphs she inscribes in others.",
            "Keeps an unfinished sculpture in her sanctum — a cradle of bone meant for a child she lost."
        ],
        role_in_campaign=(
            "Selwyn may assist with structural challenges, decipher bone glyphs, or offer sanctuary within one of her constructs. "
            "She could also become a vital ally in conflicts involving necromancy, legacy architecture, or forgotten sanctuaries."
        ),
        personality_traits=["Precise, reverent, unflinching", "Values silence as a tool of focus"],
        narrative_hooks=[
            "She may request aid in sealing a cracked maston vault before the storm season arrives.",
            "Possesses blueprints to a pre-Sundering ossuary forgotten by history — if she can be convinced to share them."
        ],
        plot_hooks_and_interactions=[
            "Could commission the party to retrieve rare bones from a battlefield before they rot.",
            "Might be the only person who can decipher a bone-encoded warning that threatens Vanith itself."
        ],
        notable_quotes=[
            "The dead still serve, if shaped correctly.",
            "I build for those who will never see it fall."
        ]
    ),
    "nyssara_thale": NPC(
        name="Nyssara Thale",
        title="Arbiter of the Rootspire Accord",
        race="Elf",
        age="122",
        pronouns="She/Her",
        alignment="Lawful Good",
        affiliation="Rootspire Council",
        aliases=["The Thorned Gavel", "Voice Beneath Bough"],
        background=(
            "Raised within the towering bough sanctums of Tel Varuun, Nyssara was groomed from childhood to wield the law with both precision and grace. "
            "She commands a quiet but firm authority, wielding centuries-old legal rites rooted in the elder flora of the region."
        ),
        overview=(
            "Dignified, diplomatic, and unnervingly still — a judge who weighs not only words but the soil they’re spoken on."
        ),
        appearance=Appearance(
            alias="Voice Beneath Bough",
            gender="Female",
            age="122",
            species="Elf",
            height="5'9\"",
            build="Slight and angular, like the branch of a silver tree",
            eyes="Verdant green with bark-like striations",
            hair="Dark brown with streaks of vine-silver, worn in coiled loops",
            skin="Smooth copper, with natural knots and ridges along the temples",
            voice="Measured and low, with a rustle to it — like parchment brushed by leaves",
            clothing="Magistrate’s robes interwoven with living threads from the Arborloom",
            accessories="Staff grown from the heartwood of a sapient fig tree, scroll-cloak with roots as hems",
            aesthetic="Natural elegance bound to structure",
            aura="Tranquility that roots itself into any room she enters",
            presence="Unmoving as a statute when still — but her words cut through noise like a falling branch",
            scent="Cedarwood and wild mint",
            description=(
                "Nyssara moves with the rhythm of Tel Varuun itself — deliberate, serene, and bound to ancient patterns of growth and law. "
                "She is both sanctuary and sentence, depending on how truth flows."
            )
        ),
        secrets=[
            "She once ruled against her own kin, whose exile later saved the city during a wildfire siege.",
            "Her staff bears a hidden blossom that only blooms during moments of personal doubt."
        ],
        motivations=[
            "Uphold the ancient Rootspire Accord that balances law, nature, and magic.",
            "Preserve the memory-grove where elder trials are stored as dreamseeds.",
            "Ensure no corruption roots itself beneath the canopy."
        ],
        weapons=None,
        known_publicly=[
            "Has never lost a deliberation to dissent — even when voting alone.",
            "Trains apprentice arbiter-keepers under moonlight rituals."
        ],
        public_knowledge=[
            "Known for settling border disputes through guided meditation and root-divination.",
            "Once mediated peace between flamekin rebels and the elder dryads."
        ],
        private_knowledge=[
            "Has forbidden herself from ever returning to her birthtree after breaking its oath.",
            "Secretly doubts whether the Accord still fits this age — but keeps rewriting it anyway."
        ],
        role_in_campaign=(
            "Nyssara can settle moral disputes, grant legal sanctuary, or provide insight into the magical foundations of Tel Varuun’s laws. "
            "She may become a powerful political ally — or the voice that condemns the party, if they upset the balance."
        ),
        personality_traits=["Calm, precise, bound to ritual and rooted values."],
        narrative_hooks=[
            "She may request help investigating a grove where the Accord’s runes have begun to decay.",
            "Holds memories in dreamseeds — one of which may contain something the party desperately needs."
        ],
        plot_hooks_and_interactions=[
            "Can offer the party protection under Accord law — but only if they fulfill a binding vow.",
            "May be the only one who can translate a dying tree’s testimony in an ancient trial."
        ],
        notable_quotes=[
            "Every oath has a root. And every root knows the truth.",
            "Justice, like a tree, cannot be rushed — but it must be tended."
        ]
    ),
    "corven_marrowheel": NPC(
        name="Corven Marrowheel",
        title="Verdancy Engineer of the Underbough Loom",
        race="Gnome",
        age="64",
        pronouns="He/Him",
        alignment="Neutral Good",
        affiliation="Guild of Living Mechanics",
        aliases=["Rootwright", "Wyrmtooth Whistler"],
        background=(
            "Once a drifting tinker from the Stonecoast, Corven found Tel Varuun not by map, but by following a sentient vine that refused to let go of his boot. "
            "Since then, he’s merged botanical lore with mechanical genius to build self-winding harvest arches and vine-fed irrigation winders."
        ),
        overview=(
            "Brilliantly distracted, whimsically inventive — Corven talks like ivy grows: fast, winding, and occasionally wrapping around your thoughts."
        ),
        appearance=Appearance(
            alias="Rootwright",
            gender="Male",
            age="64",
            species="Gnome",
            height="3'4\"",
            build="Compact and spry, with spring-loaded posture",
            eyes="Molasses brown behind spiral magnifying lenses",
            hair="Wild chestnut curls wrapped in moss twine",
            skin="Walnut-brown smudged constantly with chlorophyll and soot",
            voice="Quick, nasal, and fond of strange whistling emphasis",
            clothing="Patchwork coat of stitched burlap, leather, and flower-stamped denim",
            accessories="Multi-tool gauntlet, a sap-fed pressure gauge, and a tiny terrarium monocle",
            aesthetic="Tinker-meets-terrarium",
            aura="Buzzing with unspent ideas",
            presence="Always halfway through three things, one of which is probably growing on you",
            scent="Crushed mint, singed pollen, and warm copper",
            description=(
                "Corven’s fingers twitch even when idle, as if his hands are remembering something they haven’t built yet. "
                "He has more affection for his grafted machines than most people, but never forgets a kindness — or a good root pun."
            )
        ),
        secrets=[
            "His most successful invention — the symbiotic wind-pump — was partly designed by accident, after he tripped into a vine-rift.",
            "Keeps a hidden sketch of a machine he claims could regrow extinct flora — if the Guild ever stops laughing at it."
        ],
        motivations=[
            "Advance the fusion of greenlife and gear without violating the Rootspire Accord.",
            "Track down a rogue automoss construct he accidentally awakened.",
            "Get someone — anyone — to listen to his theory on fungal resonators and time loops."
        ],
        weapons=None,
        known_publicly=[
            "Often hires adventurers to retrieve rare seeds, spores, or machine components lost in the canopy.",
            "Invented the hummingbark harvester, which runs entirely on bees."
        ],
        public_knowledge=[
            "Has been fined six times for 'unregulated vine-lashing' in the civic rootways.",
            "Once got into a yelling match with a sapient turnip."
        ],
        private_knowledge=[
            "Believes Tel Varuun is slowly drifting off course — geologically — due to root-weight imbalance.",
            "In love with someone who doesn’t age like he does, and he won’t build the clock that could fix it."
        ],
        role_in_campaign=(
            "A whimsical quest-giver and potential builder of party upgrades. Corven may assist in navigating overgrown ruins, deciphering botanical tech, or offering absurd contraptions that somehow work."
        ),
        personality_traits=["Energetic, obsessive, endlessly curious"],
        narrative_hooks=[
            "Wants help recovering a prototype sap-seeder that went feral and took over a grove.",
            "May be the only person who knows how to safely disarm an overgrown grove reactor."
        ],
        plot_hooks_and_interactions=[
            "Could outfit the party with semi-sentient equipment… with unpredictable side effects.",
            "Has hidden plans for a weaponized root-net — might trade it for pollen from a forgotten bloom."
        ],
        notable_quotes=[
            "It hums? It’s alive. It bites? It’s *working*.",
            "Look, if it grows and it turns, it’s *basically* safe."
        ]
    ),
    "virelya_senthane": NPC(
        name="Virelya Sen'thane",
        title="Petalwright of the Bloomshade Choir",
        race="Half-Elf",
        age="29",
        pronouns="She/Her",
        alignment="Neutral",
        affiliation="Bloomshade Choir",
        aliases=["Chorus-of-Bloom", "Mistress of the Pale Canopy"],
        background=(
            "A child of spring hail and whisperleaf, Virelya was raised in the voice-shrouded courts beneath the flowering canopies of Tel Varuun. "
            "Trained in floral symphonics and the ritual arrangement of bloom-sequences, she leads ceremonies that stir memory, heal grief, or silence pain entirely."
        ),
        overview=(
            "A poet in posture and tone, Virelya embodies calm reverence. Her every movement seems choreographed by the seasons themselves."
        ),
        appearance=Appearance(
            alias="Chorus-of-Bloom",
            gender="Female",
            age="29",
            species="Half-Elf",
            height="5'6\"",
            build="Graceful, long-limbed, with soft tapering movements",
            eyes="Iridescent lavender with flecks of pollen gold",
            hair="Ash-blonde, braided with living blossoms that open or close with her mood",
            skin="Pale cream with faint rose-tinted undertones",
            voice="Melodic, mezzo-soprano, speaks in slow cadences",
            clothing="Layered silk robes dyed from windflower pigments, trailing petals that never wilt",
            accessories="Ceremonial shears shaped like a crescent moon, flower-sigil diadem",
            aesthetic="Sacred botanist meets silent bard",
            aura="Tranquil and wistful — like walking into a garden after rain",
            presence="Weightless yet commanding, like petals drifting toward the earth",
            scent="Blooming jasmine, crushed violet, and distant honey",
            description=(
                "Virelya does not need to raise her voice to be heard. Her presence is a ritual unto itself — calming, binding, and strangely unforgettable. "
                "She walks the boundary between ceremony and spell, and those caught in her rites rarely wish to leave."
            )
        ),
        secrets=[
            "Her floral rites are not merely symbolic — they tap into an ancient memory-weave that predates Tel Varuun’s founding.",
            "Her tears carry a faint numbing effect — the residue of a pact she once made with a mourning spirit."
        ],
        motivations=[
            "Preserve the fading bloom-tongue language before it’s lost to silence.",
            "Reseed the Witherfields with emotion-healing flora.",
            "Find the one who once sang in harmony with her, before vanishing during a midsummer rite."
        ],
        weapons=None,
        known_publicly=[
            "Performs rites at dawn and dusk that draw crowds into quiet weeping or peaceful trance.",
            "Wears no shoes — claims the soil remembers better that way."
        ],
        public_knowledge=[
            "Tutors apprentices in the five petal-chords — tonal rituals for memory restoration.",
            "Believed to be favored by an ancient floral spirit known only as the Petalshade."
        ],
        private_knowledge=[
            "Fears she’s beginning to forget the sacred melodies — and what they meant.",
            "Harbors guilt for altering a funeral rite to ease a grieving noble’s pain… against the will of the dead."
        ],
        role_in_campaign=(
            "Virelya may assist with memory-based magic, grief rituals, or emotional healing. "
            "She could also unlock buried dreams, translate ancient flora-bound spells, or weave sorrow into something sacred."
        ),
        personality_traits=["Serene, enigmatic, tender-hearted beneath layers of formality"],
        narrative_hooks=[
            "May seek the party’s help retrieving a stolen flower-scroll from a ruined bloomshrine.",
            "Wishes to heal a cursed forest but requires an emotion the party no longer remembers."
        ],
        plot_hooks_and_interactions=[
            "Can perform a Rite of Unburdening that might erase a memory… or expose a hidden truth.",
            "Possesses knowledge of a forgotten floral dialect key to unsealing a deep grove tomb."
        ],
        notable_quotes=[
            "We do not bury the past — we let it bloom in silence.",
            "Some griefs do not end. But they can be softened, petal by petal."
        ]
    ),
    "deyra_varn": NPC(
        name="Deyra Varn",
        title="Warden of the Fogholt",
        race="Human",
        age="36",
        pronouns="She/Her",
        alignment="Neutral",
        affiliation="Saltwatch of Salkir",
        aliases=["Mistblade", "Graymark Warden"],
        background=(
            "Deyra was born in the drowned hamlet of Barrowhull, her family swallowed by the moor when she was a child. "
            "Raised by the Saltwatch, she grew into a peerless ranger and boundary-keeper, sworn to defend the living from the drowned dead — and the drowned from the living."
        ),
        overview=(
            "Terse, watchful, and carved from discipline, Deyra sees things others miss — not because she’s gifted, but because she never stops looking."
        ),
        appearance=Appearance(
            alias="Mistblade",
            gender="Female",
            age="36",
            species="Human",
            height="5'8\"",
            build="Lean and rangy, hardened by long nights in the moor",
            eyes="Steel blue, always narrowed as if squinting through mist",
            hair="Dark ash-brown, braided tightly and wrapped in a salt-dyed kerchief",
            skin="Weathered umber with pale scars down one cheek",
            voice="Low and gravelled, but firm and clear in crisis",
            clothing="Salt-damp leather coat with a long moor-cloak, mossproof greaves",
            accessories="Fogglass lens, curved shortblade etched with warding runes, bleached antler whistle",
            aesthetic="Haunted ranger meets ritual scout",
            aura="Silent pressure — like something always watching",
            presence="Always near the edge of sight, rarely center stage",
            scent="Wetted stone, river rot, burnt sage",
            description=(
                "Deyra’s presence is the moor itself — not loud, not bold, but *there*, even when you wish it weren’t. "
                "She walks where others drown, guided by a memory no one else wants to remember."
            )
        ),
        secrets=[
            "She speaks to something beneath the fog — and it answers in her dreams.",
            "The blade she carries was taken from a drowned knight who rose and called her by name… before crumbling into brine."
        ],
        motivations=[
            "Keep the drowned bound to the moor and the living from disturbing their sleep.",
            "Discover what cracked the fog-holds in the southern fen.",
            "Uncover the source of the sudden stillness near Old Hollowmere."
        ],
        weapons=["Fogblade (ghost-steel shortblade)", "Moor-whistle (for summoning aid or warnings)"],
        known_publicly=[
            "Knows every foot of the salt paths and where not to tread.",
            "Hasn’t missed a dusk patrol in twelve years."
        ],
        public_knowledge=[
            "Once dragged a full wagonload of survivors out of a moor-collapse alone.",
            "Wears a braid-knot that signifies mourning — but won’t say for whom."
        ],
        private_knowledge=[
            "Feels the fog creeping into her — she’s starting to *see* things before they happen.",
            "Keeps a list of names in her coat, all marked with drown-dates yet to come."
        ],
        role_in_campaign=(
            "A guide through cursed moors, a grim ally against incorporeal threats, or a grim reaper with empathy. "
            "May warn the party of dangers before they’re ready — or vanish just before they arrive."
        ),
        personality_traits=["Taciturn, alert, iron-hearted"],
        narrative_hooks=[
            "She may request help investigating a moorlight sighting no one else believes in.",
            "Carries a relic found at the edge of the Blackmere that hums in the party’s presence."
        ],
        plot_hooks_and_interactions=[
            "Could become cursed by the moor’s ghosts mid-campaign — requiring the party to decide if she’s still on their side.",
            "Knows a secret path into the drowned sanctum of Barrowhull, but demands a steep oath in return."
        ],
        notable_quotes=[
            "Don’t trust what walks on dry ground here — especially if it *shouldn’t*.",
            "You’re not lost until the fog forgets your name. After that, you’re theirs."
        ]
    ),
    "calder_vesh": NPC(
        name="Calder Vesh",
        title="Miretongue of the Brine Sepulcher",
        race="Half-Orc",
        age="47",
        pronouns="He/Him",
        alignment="Chaotic Neutral",
        affiliation="Order of the Drowned Word",
        aliases=["Brine-Eyed", "Whispershell"],
        background=(
            "Once a heretic preacher from the river-choked town of Kelth’s Wane, Calder found his calling not in flame or sermon, but in the slow murmur of the moor. "
            "He claims the drowned speak, and he listens. His followers — few but fervent — say he’s touched by something older than tide or time."
        ),
        overview=(
            "Eloquent, unsettling, and messianic in mood, Calder walks with both madness and clarity whispering in tandem beneath his tongue."
        ),
        appearance=Appearance(
            alias="Brine-Eyed",
            gender="Male",
            age="47",
            species="Half-Orc",
            height="6'0\"",
            build="Broad-shouldered, hunched from years of crouching near water’s edge",
            eyes="Pale green veined with milky swirls, unfocused but seeing too much",
            hair="Long and sea-damp, tied in a leather cord draped with eel bones",
            skin="Gray-olive, blotched from fungal exposure and moorlight radiation",
            voice="Thick, wet, and lilting — as if spoken from behind water",
            clothing="Tattered priest-robes coated with saltfilm and moss",
            accessories="Necklace of driftglass tongues, barnacle-carved reliquary",
            aesthetic="Swamp prophet meets drowned relic-keeper",
            aura="Claustrophobic calm — like kneeling in a flooded crypt",
            presence="Simultaneously magnetic and repellant, like knowing you *shouldn't* look — but do anyway",
            scent="Salt brine, decayed kelp, river incense",
            description=(
                "Calder speaks slowly, deliberately, and with words that seem borrowed from someone — or something — else. "
                "His followers mark their foreheads with salt, and some claim he’s never blinked during a sermon."
            )
        ),
        secrets=[
            "He swallowed a glyph-stone pulled from a drowned saint’s jaw — and it has never stopped whispering.",
            "The reliquary he wears contains water that never evaporates — and may be alive."
        ],
        motivations=[
            "Translate the complete Drowned Litany buried beneath Hollowmere.",
            "Unite the scattered Tidebound cults under his murmur.",
            "Uncover the origin of the singing bones found after each storm."
        ],
        weapons=["Ceremonial blade carved from whale cartilage (ritual use only)"],
        known_publicly=[
            "Holds sermons on the edge of the blackmere in the dead of night.",
            "Refuses to walk on bridges — only wades, barefoot, even in winter."
        ],
        public_knowledge=[
            "Was exiled from Kelth’s Wane for blaspheming both church and tide in the same breath.",
            "Sometimes speaks in a tongue no scholar can place — not even himself."
        ],
        private_knowledge=[
            "He does not sleep. He listens. And when he tries not to… it *gets louder*.",
            "He once drowned a friend to prove a point — and the body was never found."
        ],
        role_in_campaign=(
            "Calder can act as an oracle, mad seer, or bearer of moor-doom. "
            "He may hold vital knowledge no sane soul would trust — or offer insight at the cost of something precious."
        ),
        personality_traits=["Ritualistic, slow-speaking, disturbingly serene"],
        narrative_hooks=[
            "Requests the party retrieve a relic from the flooded vault of a forgotten tide-chapel.",
            "Might offer to bind a party member’s wounds… in return for a whispered truth they must never share."
        ],
        plot_hooks_and_interactions=[
            "Holds partial knowledge of a drowning ritual that could suppress ghosts — or invite something worse.",
            "May be hunted by an old faith — or courted by one even older."
        ],
        notable_quotes=[
            "The tide remembers. Even if it must pull you under to teach you.",
            "Not all voices above the water are living. And not all silence is peace."
        ]
    ),
    "marreth_quince": NPC(
        name="Marreth Quince",
        title="Lantern-Keeper of the Wending Path",
        race="Halfling",
        age="53",
        pronouns="They/Them",
        alignment="Neutral Good",
        affiliation="Wayfarer’s Vigil",
        aliases=["The Last Light", "Mistwalker Quince"],
        background=(
            "Marreth has kept the Wending Path lit for over three decades — the moor's only semi-reliable road. "
            "Each dusk, they walk it end to end with their weathered lantern, ensuring no travelers stray into the mist... and no *others* find their way out."
        ),
        overview=(
            "Wry, kind-eyed, and stubborn as driftwood, Marreth seems ageless in the way only those who refuse to stop *being needed* can be."
        ),
        appearance=Appearance(
            alias="Mistwalker Quince",
            gender="Nonbinary",
            age="53",
            species="Halfling",
            height="3'1\"",
            build="Sturdy and slightly stooped from nightly walks",
            eyes="Warm amber with crow’s feet etched deep",
            hair="White-blond, cropped short and hidden under a waxed oilskin hood",
            skin="Mottled peach, lightly weatherworn",
            voice="Comforting alto with a slight rasp, like wind across reeds",
            clothing="Layered wool-and-leather duster lined with water-repelling glyphs",
            accessories="Lantern of waking flame, charms made of old buttons, copper, and teeth",
            aesthetic="Moor shepherd meets storykeeper",
            aura="Faint and steady, like a hearthfire down a long road",
            presence="Unassuming but magnetic — people find themselves safer just standing near them",
            scent="Old smoke, marshgrass, warm cider",
            description=(
                "Marreth doesn't walk fast, but no one ever loses sight of their lantern. "
                "Their laugh is quiet and often comes with a ghost story you weren’t ready for — but that somehow comforts you anyway."
            )
        ),
        secrets=[
            "They once guided a ghost along the full path, and it never returned.",
            "The lantern they carry doesn’t burn oil — it burns *memory*, and it’s nearly full."
        ],
        motivations=[
            "Protect those traveling the moor — living or dead.",
            "Maintain the fading glyphs that keep the Wending Path from shifting.",
            "Record every strange encounter in their worn, waterproof journal."
        ],
        weapons=["Lantern (blinds incorporeal undead)", "Walking stick with hidden silver blade"],
        known_publicly=[
            "Has never missed a night-walk — not in 30 years.",
            "Trained every current member of the Wayfarer’s Vigil."
        ],
        public_knowledge=[
            "Knows every crossroad, corpse-marker, and sinkhole on the Wending Path.",
            "Said to have once led a cursed caravan safely through by *singing* all night."
        ],
        private_knowledge=[
            "They don’t know how much longer the lantern will burn — and they’re afraid of what happens when it goes out.",
            "Sometimes whispers names while walking alone. Names no one recognizes. Names that answer."
        ],
        role_in_campaign=(
            "Marreth is a guide, a guardian, and a living storybook. "
            "They can provide safe passage through cursed areas, help track incorporeal foes, or offer vital context to moor legends."
        ),
        personality_traits=["Steady, warm, fond of dry humor", "Never turns away a wanderer"],
        narrative_hooks=[
            "Might ask the party to recover a stolen flame-keystone from a cult trying to reroute the Path.",
            "Could invite the party to walk with them — and witness something *only seen by lanternlight.*"
        ],
        plot_hooks_and_interactions=[
            "The lantern’s power may begin to fade, forcing Marreth to seek a new bearer — perhaps among the party.",
            "They know a secret path to the ruins of Barrowhull, but the road is *only visible when sung.*"
        ],
        notable_quotes=[
            "Moor’ll swallow the loud first. Walk quiet, carry a bright story.",
            "You don’t find your way here. The Path finds *you.*"
        ]
    ),
    "lurga_tharnforge": NPC(
        name="Lurga Tharnforge",
        title="Matron-Commander of the Stonewake Guard",
        race="Dwarf",
        age="142",
        pronouns="She/Her",
        alignment="Lawful Neutral",
        affiliation="Stonewake Guard",
        aliases=["The Chain-Mother", "Breaker of Vows"],
        background=(
            "Born beneath the Ironroot Vaults, Lurga rose from sentry to high commander through relentless discipline, battlefield genius, and a refusal to die where others would kneel. "
            "She unified the fragmented guard posts of Drosven Hold after the Blackblood Rebellion, forging them into the Stonewake Guard."
        ),
        overview=(
            "Immovable, steel-eyed, and fiercely traditional — Lurga does not *lead* so much as *drag destiny by its beard into formation.*"
        ),
        appearance=Appearance(
            alias="Breaker of Vows",
            gender="Female",
            age="142",
            species="Dwarf",
            height="4'9\"",
            build="Stocky, broad-shouldered, with arms like quarry cranes",
            eyes="Molten bronze, flecked with iron",
            hair="Thick black, braided into four plaits — one for each oath kept",
            skin="Ashen tan with roughness earned, not inherited",
            voice="Deep contralto, clipped and decisive like a smith’s chisel",
            clothing="Full battle regalia of the Stonewake — lacquered black steel, crimson cape, iron gorget bearing twenty clan sigils",
            accessories="Oath-chain belt, carved bone rings from fallen allies, war-horn etched in obsidian",
            aesthetic="Warlord-matriarch bound by code and consequence",
            aura="Searing conviction, like standing too close to a forge left burning overnight",
            presence="Commands stillness — silence follows her like a cloak",
            scent="Hot iron, old parchment, and cave myrrh",
            description=(
                "Lurga is a living standard — a symbol as much as a soldier. "
                "To speak over her is to dishonor the forge. To *fail* her… is to vanish like a brittle chain in winter."
            )
        ),
        secrets=[
            "Her war-horn sounds only once per decade — and when it does, no one who hears it sleeps soundly again.",
            "She bears a forbidden glyph scar sealed beneath her chestplate — earned in a duel with a traitor brother."
        ],
        motivations=[
            "Defend Drosven Hold from internal corruption and outer siege alike.",
            "Ensure the unity of the guard — and punish those who seek to fracture it.",
            "Locate the missing second fragment of the Stonewake Charter."
        ],
        weapons=["Twin hooked hammers, steel-whorled with oathbinding runes"],
        known_publicly=[
            "Has never been defeated in formal combat.",
            "Demands her troops memorize the names of every citizen — alive or entombed."
        ],
        public_knowledge=[
            "Once walked barefoot through a fire-rift to rescue a collapsing squad — returned singing an old war dirge.",
            "Leads morning oaths herself. Every day. No exceptions."
        ],
        private_knowledge=[
            "Fears she is training successors for a war that cannot be won — only delayed.",
            "Wrote a forbidden will ceding command to someone outside the bloodclans, should she fall dishonorably."
        ],
        role_in_campaign=(
            "Lurga may offer the party protection, military resources, or dangerous intelligence — but only if they prove themselves worthy. "
            "Her trust, once broken, cannot be reforged."
        ),
        personality_traits=["Commanding, principled, proud to a fault"],
        narrative_hooks=[
            "May call upon the party to uncover a saboteur within the Stonewake ranks.",
            "Might offer an ancient relic if the party succeeds in passing her trial of chains."
        ],
        plot_hooks_and_interactions=[
            "Could become a temporary ally during a siege, altering the tide if won over.",
            "Her oath-scar may react to a glyph the party uncovers — binding her fate to theirs, unwillingly."
        ],
        notable_quotes=[
            "Steel can lie. But chain remembers.",
            "Swear nothing lightly in my hold — or you’ll carry the weight with your spine."
        ]
    ),
    "vaeren_soln": NPC(
        name="Vaeren Soln",
        title="Archivist of the Writ Deep",
        race="Half-Elf",
        age="61",
        pronouns="He/Him",
        alignment="Lawful Neutral",
        affiliation="Deep Scrivener's Guild",
        aliases=["Inkwarden", "The Quill Bastion"],
        background=(
            "Vaeren was orphaned in a breach-collapse during the War of Deep Knots. Raised within the Writ Deep — the vast hollow-scroll vaults beneath Drosven Hold — he has spent his life curating battle oaths, exile ledgers, and silence-pacts bound in bloodwax. "
            "He is less a scholar than a steward of buried promises."
        ),
        overview=(
            "Cerebral, sharp-tongued, and ruthlessly precise, Vaeren defends the written word with a zeal most reserve for sword and flame."
        ),
        appearance=Appearance(
            alias="Inkwarden",
            gender="Male",
            age="61",
            species="Half-Elf",
            height="5'11\"",
            build="Lithe with a scribe’s grace, marred by a slight stoop from years hunched over stone-tablets",
            eyes="Pale citrine — piercing and cold",
            hair="Ink-black, streaked silver, tied into a low cord-bound bun",
            skin="Parchment-pale with calloused fingers permanently stained by wax and ink",
            voice="Precise, clipped diction — like reading aloud even when speaking",
            clothing="Formal robes of the Scrivener’s Guild, layered with tabards of char-red silk and etched leather",
            accessories="Ledger-lock rings, inkvial necklace, wand of lignified charcoal",
            aesthetic="Legalist archivist armed with ancient law instead of blades",
            aura="Measured gravity — like entering a courtroom built from quiet stone",
            presence="Commands attention through unspoken weight, not volume",
            scent="Vellum, scorched cedar, and sealing wax",
            description=(
                "Vaeren walks like someone balancing truths too heavy for one lifetime. "
                "He greets even old friends with full name and title, and will correct your grammar mid-scream if you die incorrectly."
            )
        ),
        secrets=[
            "Keeps an unauthorized codex of forbidden glyph contracts sealed in molten amber — its lock responds only to truthfully spoken regrets.",
            "Once erased a noble’s lineage from the scrolls in exchange for their silence about a massacre no one survived to witness."
        ],
        motivations=[
            "Preserve the inviolability of written oaths across all territories.",
            "Recover the last three pages of the Lost Charter of Unmaking.",
            "Ensure Drosven law is not rewritten by bloodshed, but by proof."
        ],
        weapons=["Wand of silencing script (can suppress spoken lies)"],
        known_publicly=[
            "Refuses to speak informally — even while drinking.",
            "Knows every exile sentence issued in the last two centuries, by memory."
        ],
        public_knowledge=[
            "Once debated a High Warlord into surrender during the Siege of Hornspire, using only treaty clause citations.",
            "Believed to have never smiled — though a few say they’ve heard him laugh. Once."
        ],
        private_knowledge=[
            "Grieves a lover who vanished between clauses — quite literally, mid-vow.",
            "Believes the Hold is heading toward a legal schism no one else sees coming."
        ],
        role_in_campaign=(
            "Vaeren can serve as legal counsel, treaty broker, or revelator of ancient oaths the party unknowingly triggered. "
            "He may also serve as an ally — or enemy — when the party’s choices cross the letter of old laws."
        ),
        personality_traits=["Precise, principled, quietly severe"],
        narrative_hooks=[
            "May request the party retrieve an oathstone from a tomb sealed by glyph-law centuries ago.",
            "Might offer help deciphering a player’s curse — if it involves a miswritten soul-pact."
        ],
        plot_hooks_and_interactions=[
            "Could intervene in a trial or judgment against the party, offering defense — or prosecution.",
            "His codex may hold the party’s name, inked centuries before they were born."
        ],
        notable_quotes=[
            "Law is not justice. But it *remembers.*",
            "Ink is cheaper than blood. But harder to wash away."
        ]
    ),
    "kaela_emberwright": NPC(
        name="Kaela Emberwright",
        title="Pyrestoke Artificer of the Ember Reliquary",
        race="Gnome",
        age="65",
        pronouns="She/Her",
        alignment="Chaotic Good",
        affiliation="Ember Reliquary Guild",
        aliases=["Brightforged", "Ash-Tongue"],
        background=(
            "Hailing from the basalt-hewn villages just outside Drosven’s lowest gate, Kaela climbed — sometimes literally — into the Reliquary’s forbidden tier. "
            "She reverse-engineered a broken glyph engine at age thirteen, laughed through the inquisition that followed, and now designs sacred flame-artifacts for Drosven's most secretive wars."
        ),
        overview=(
            "Energetic, irreverent, and recklessly brilliant, Kaela defies Drosven's stone solemnity like a spark beneath granite — chaotic, vital, and impossible to fully contain."
        ),
        appearance=Appearance(
            alias="Ash-Tongue",
            gender="Female",
            age="65",
            species="Gnome",
            height="3'6\"",
            build="Compact and wiry, all coiled tension and kinetic energy",
            eyes="Bright copper with flickering embers for pupils (a side effect)",
            hair="Charred red, frizzed wild, tied with brass gears and sootlace",
            skin="Soot-dusted tan, tattooed with flame schematics and tinker's runes",
            voice="Sharp mezzo, rapid-fire with frequent cackles",
            clothing="Layered leathers, scorched apron, bandolier of ignition crystals",
            accessories="Goggles stained with blast soot, six-fingered welding glove (self-made), braid-chime that rings when she lies (usually)",
            aesthetic="Artificer-chaos meets sacred flamekeeper",
            aura="Volatile warmth — like a forge that's *almost* safe to touch",
            presence="Instantly magnetic, like a fire you know will burn you but step closer to anyway",
            scent="Brimstone, copper dust, and cherry pipe-smoke",
            description=(
                "Kaela doesn’t just tinker — she dances with combustion. Her workshop has exploded twice, her apprentices speak in riddles now, and no one dares challenge her glyph-patents in court. "
                "Some say her heartbeat ticks in time with a fire engine that never cooled."
            )
        ),
        secrets=[
            "She reassembled a sealed glyph relic — and didn’t turn it *off*. It’s still ticking in her workshop, hidden beneath twenty feet of bedrock.",
            "Once forged an artifact that 'accidentally' reversed entropy. She keeps it in a lunchbox labeled 'DO NOT FEED'."
        ],
        motivations=[
            "Prove that flame isn’t just destruction — it’s memory, motion, rebirth.",
            "Crack the code behind a burnt pre-Glyphic schematic sealed in ashglass.",
            "Create an autonomous flame-being capable of mourning the dead."
        ],
        weapons=["Blast-wand (unstable, experimental)", "Wrenchblade (doubles as a longscrew crowbar)"],
        known_publicly=[
            "Can ignite stone with her fingers. Claims it’s science. No one believes her.",
            "Once turned the entire eastern forgehall into a walking siege platform — for two hours."
        ],
        public_knowledge=[
            "Banned from the upper archives after attempting to 'improve' the fire suppression glyphs.",
            "Wears a ring inscribed 'I regret nothing' — it's on her welding hand."
        ],
        private_knowledge=[
            "Hears voices in the forge — not whispers, but *laughter* she can’t trace.",
            "Believes she has one great invention left before the fire takes her… and she's ready."
        ],
        role_in_campaign=(
            "Kaela can offer explosive prototypes, dangerously useful devices, or insight into relics too unstable for anyone else to touch. "
            "She may also need help containing (or recovering) something she accidentally unleashed."
        ),
        personality_traits=["Unapologetically curious, mischievous, quick-tempered but faster to laugh"],
        narrative_hooks=[
            "Might offer the party an experimental item — but forgets to mention the 'emotional instability' clause.",
            "Asks for rare heat-crystals buried beneath a collapsing mine with *sentient magma.*"
        ],
        plot_hooks_and_interactions=[
            "Her ticking relic may draw the interest of the Sigil Covenant… or awaken something worse.",
            "Kaela’s final invention could reshape Drosven’s fate — if it doesn’t eat her first."
        ],
        notable_quotes=[
            "You see an accident. I see a prototype with ambition.",
            "Fire’s never truly safe. But neither is hope."
        ]
    ),
    "siryne_morlaith": NPC(
        name="Siryne Morlaith",
        title="Dirge-Seer of the Drowned Choir",
        race="Elf (Undertide-blooded)",
        age="117",
        pronouns="She/Her",
        alignment="Neutral",
        affiliation="Drowned Choir of Nhalm",
        aliases=["The Mourning Veil", "Weeper-in-Stillness"],
        background=(
            "Once a noble scion of the drowned spires of Liraevan, Siryne walked into Nhalm’s Wake on the night the waters stopped falling — and never left. "
            "She claims the flood took more than her kin; it rewrote her voice into lamentation, and bound her to the undertide’s memory."
        ),
        overview=(
            "Elegant, spectral, and unyieldingly solemn, Siryne speaks rarely — but when she does, the dead still to listen."
        ),
        appearance=Appearance(
            alias="The Mourning Veil",
            gender="Female",
            age="117",
            species="Elf (Undertide-blooded)",
            height="5'10\"",
            build="Slender, almost weightless in motion",
            eyes="Pale violet rimmed in silver tears",
            hair="Flowing river-black, veiled with glimmerthread netting",
            skin="Luminescent pearl-gray, marbled faintly with blue",
            voice="Echoing alto, layered as if underwater",
            clothing="Ceremonial vestments of the Drowned Choir, adorned in flood-glyph lace",
            accessories="Necklace of kelp-glass tears, flood-chime anklet, veiled circlet of tide silver",
            aesthetic="Water-priestess elegy made flesh",
            aura="Soft sorrow, pressing like deep water on the ribs",
            presence="Commands reverence and ache — like hearing a hymn sung at a funeral you forgot attending",
            scent="Salted lilies, petrichor, forgotten prayers",
            description=(
                "Siryne moves as though half-dreaming, trailing song that doesn't require breath. "
                "She remembers what even the waters forgot, and weeps not out of grief — but duty."
            )
        ),
        secrets=[
            "Siryne’s song can still a ghost’s hunger — or call it to feast.",
            "She is not truly alive — nor is she dead. The undertide holds her in sacred suspension, its emissary to the breathing world."
        ],
        motivations=[
            "Preserve the death-songs of those lost to the drowned cities.",
            "Hold the flood’s memory intact — no matter the cost.",
            "Prevent the awakening of the Bell That Was Buried."
        ],
        weapons=["Dirgeblade (sings as it strikes, grief-forged)"],
        known_publicly=[
            "Can calm restless spirits with a single refrain.",
            "Refuses to walk on dry earth — travels only through mist or over water."
        ],
        public_knowledge=[
            "Siryne leads the Lament Vigil every solstice — and the fog always deepens during her songs.",
            "Some say she can speak to those drowned long ago… even those never named."
        ],
        private_knowledge=[
            "She is bound by covenant to never love again — the vow was taken in return for her voice.",
            "She hears the Bell even now — and believes it will soon ring."
        ],
        role_in_campaign=(
            "A ritualist, guide, or gatekeeper to undertide secrets — Siryne may help the party traverse haunted waters, bargain with the dead, or silence a rising threat from beneath the floods."
        ),
        personality_traits=["Gentle, mournful, firm in mystery"],
        narrative_hooks=[
            "Might ask the party to recover a relic-song lost in a sunken vault.",
            "Could offer protection from haunting — but demands a memory in return."
        ],
        plot_hooks_and_interactions=[
            "The Bell That Was Buried may stir in the party’s presence — and she may beg them to flee, or to stop it.",
            "A party member’s dream may echo one of her laments — and she *knows* why."
        ],
        notable_quotes=[
            "The flood does not forgive. It only forgets more slowly than we do.",
            "If you weep in Nhalm, do so with purpose — or it will answer you."
        ]
    ),
    "garrun_fellmark": NPC(
        name="Garrun Fellmark",
        title="Mistwarden of the Bell-Gates",
        race="Human",
        age="38",
        pronouns="He/Him",
        alignment="Lawful Neutral",
        affiliation="Wardens of Nhalm",
        aliases=["The Silent Gate", "Fog-Locked Sentinel"],
        background=(
            "Born to a family long tasked with watching the fog-throttled passes that ring Nhalm’s barrowlands, Garrun took his vow of silence at twelve and has spoken no word since. "
            "He alone tends the rusted bell-chains and spectral wards that bind the thresholds between the drowned and the breathing."
        ),
        overview=(
            "Still as a grave-moon, unflinching as tombstone shadow — Garrun is the guardian of doors never meant to open again."
        ),
        appearance=Appearance(
            alias="The Silent Gate",
            gender="Male",
            age="38",
            species="Human",
            height="6'2\"",
            build="Lean, weather-hardened, posture squared with trained purpose",
            eyes="Steel blue veined with white — as if perpetually backlit by fog",
            hair="Dark brown, shaved at the sides, long on top and braided into the back of his collar",
            skin="Pale ochre, speckled with windburn and ward-scars",
            voice="Mute — speaks only with gesture, whistle, or bell-tongue",
            clothing="Heavy moor cloak with fogglyph embroidery, oilskin layers, and clasped runes of ashwood",
            accessories="Belt of six tuning bells, fog-mirror charm, tarnished oath ring",
            aesthetic="Misty grave-warden meets ritual sentinel",
            aura="Muted intensity — like something waiting to strike but never does",
            presence="Commands respect through stillness, not force",
            scent="Old brass, mist-damp stone, peat-smoke",
            description=(
                "Garrun does not hurry. He appears when needed, vanishes when not. "
                "His signals — soft bell tolls, finger taps, mirror flashes — carry meaning far deeper than words ever could."
            )
        ),
        secrets=[
            "Garrun was born mute — but once, at age fifteen, he screamed. It split a mirror to the undertide. No one speaks of it.",
            "He guards not just the gate — but the memory of what once came through. Something that hasn't yet *finished coming through.*"
        ],
        motivations=[
            "Keep the Bell-Gates sealed — or open them only for the worthy dead.",
            "Complete the forgotten toll-pattern his ancestors died failing to finish.",
            "Protect the town from a shadow that waits for his failure."
        ],
        weapons=["Twin bell-hooks (can disable ghosts or redirect them)"],
        known_publicly=[
            "Never speaks, but hears everything.",
            "Can silence an entire square by raising one hand."
        ],
        public_knowledge=[
            "Saved a caravan from phantoms by tolling a forbidden pattern — and hasn’t slept since.",
            "Forges his own bells from alloyed grief-metal and mistbound silver."
        ],
        private_knowledge=[
            "One of the gates no longer answers his touch. He fears it is waking without him.",
            "He wears a second oath ring — hidden — to a lover who died without rites."
        ],
        role_in_campaign=(
            "Garrun can guide the party through cursed fog, guard rituals, or stand as the final barrier before something unspeakable breaches. "
            "His silence carries weight — and may one day shatter."
        ),
        personality_traits=["Watchful, grave, fiercely dependable"],
        narrative_hooks=[
            "Might beckon the party to follow during a sudden mistfall — no words, just bells and purpose.",
            "Could need aid reforging a cracked bell before the next lunar convergence."
        ],
        plot_hooks_and_interactions=[
            "A party member might dream of Garrun's bell — before ever meeting him.",
            "He may offer to ring a truth from one of the players — but warns it cannot be unlearned."
        ],
        notable_quotes=[
            "*[Silent — but tolls a bell four times in perfect descending sequence]*",
            "*[Signs: ‘The mist knows names we’ve buried. Do not speak yours aloud tonight.’]*"
        ]
    ),
    "alenna_vire": NPC(
        name="Alenna Vire",
        title="Floodscribe of the Last Ledger",
        race="Half-Elf",
        age="34",
        pronouns="She/Her",
        alignment="Neutral Good",
        affiliation="The Archivum Drowned",
        aliases=["Inkwept", "She-Who-Keeps-the-Names"],
        background=(
            "Alenna was once a city clerk in northward Darshade before the Collapse. She arrived at Nhalm’s Wake with ink-stained fingers, a fractured memory, and a vow to remember everyone who died unseen. "
            "She now serves as Floodscribe, transcribing drowned names, ghost-heard prayers, and vanishing glyphs into the Last Ledger — a tome that forgets *nothing*, not even dreams."
        ),
        overview=(
            "Compassionate, brilliant, and quietly tenacious, Alenna is one of the few living who still writes the dead into history — not as ghosts, but as people who mattered."
        ),
        appearance=Appearance(
            alias="Inkwept",
            gender="Female",
            age="34",
            species="Half-Elf",
            height="5'6\"",
            build="Slim, academic, with posture half-guarded, half-hopeful",
            eyes="Sea-glass green with gold-flecked sclera (a result of reading the drowned ink)",
            hair="Black-brown, long and tied with ribbon markers for names she’s yet to write",
            skin="Warm beige with faint ink-bloom stains across her forearms and palms",
            voice="Gentle, often reads aloud even when not speaking to anyone",
            clothing="Practical robes inked with waterproofing runes, high-collared to hide glyph-burn scars",
            accessories="Steel stylus set, memory-vial necklace, bound quill crafted from undertide gull feather",
            aesthetic="Scholar-gravedigger — gentle resolve etched in every line",
            aura="Subtle gravity, like a story that refuses to be forgotten",
            presence="Quiet but undeniable — you feel catalogued the moment she sees you",
            scent="Ink, seafoam, damp vellum",
            description=(
                "Alenna walks with urgency but no haste — as though every step risks losing a name. "
                "She does not cry, but sometimes her ink wells shimmer strangely, as if remembering sorrow too deep for speech."
            )
        ),
        secrets=[
            "The Last Ledger sometimes writes *on its own* — and never lies.",
            "Alenna once scribed a name she had never heard — and a day later, that person *died.* She’s afraid to write again."
        ],
        motivations=[
            "Record all who’ve been lost to the Wake and its curses.",
            "Uncover who created the Last Ledger — and what it’s truly meant to remember.",
            "Ensure no soul is erased simply because the flood stole the ink."
        ],
        weapons=["Inkblade quill (carves glyphs into memory, not flesh)"],
        known_publicly=[
            "Can write the name of the dead and *see* their last thoughts.",
            "Never refuses a name — even from ghosts, even from enemies."
        ],
        public_knowledge=[
            "Carries the Last Ledger everywhere. It’s written in languages that no longer exist.",
            "Known to vanish during storm-nights, returning with new entries and trembling hands."
        ],
        private_knowledge=[
            "She is beginning to forget her *own* name — the Ledger’s toll may be consuming her memory.",
            "The ink she uses is drawn from a drowned well no one can find on maps."
        ],
        role_in_campaign=(
            "Alenna may serve as a historian, cursebreaker, or truth-gatherer — especially when the party needs to understand an unseen legacy or stop someone from being erased."
        ),
        personality_traits=["Empathetic, meticulous, burdened with gentle purpose"],
        narrative_hooks=[
            "Might beg the party to recover a lost page — one that holds a name none of them remember writing.",
            "May warn the party they’re being forgotten — and offer to anchor them to the world through ink."
        ],
        plot_hooks_and_interactions=[
            "The Last Ledger may begin writing *about* the party — and not all entries match what truly happened.",
            "An enemy seeks to burn a page she has hidden — a page that could undo them utterly."
        ],
        notable_quotes=[
            "Ink is how we breathe after death. Let me write you down before the flood steals you.",
            "You are not forgotten. You are written. That is enough… for now."
        ]
    ),
    "maereth_kaelthorn": NPC(
        name="Maereth Kaelthorn",
        title="High Arbiter of the Thunder Bench",
        race="Half-Orc",
        age="52",
        pronouns="She/Her",
        alignment="Lawful Neutral",
        affiliation="Judiciary of Skel Vanith",
        aliases=["Stormjudge", "Voice of the Verdict"],
        background=(
            "Maereth was born during a storm so violent it shattered three court-chimes. Raised in the Vault of Civic Accord, she was schooled in both rhetoric and blade-law. "
            "She ascended the Bench not through influence, but by rendering judgments no one else dared voice — and enforcing them with thunder-backed authority."
        ),
        overview=(
            "Commanding, unshakable, and sharply intelligent — Maereth is Skel Vanith's embodiment of law sharpened into strike."
        ),
        appearance=Appearance(
            alias="Stormjudge",
            gender="Female",
            age="52",
            species="Half-Orc",
            height="6'5\"",
            build="Broad-shouldered, powerful with weight behind every step",
            eyes="Pale silver with flickering sparks of blue — a mark of her Bench Rite",
            hair="Slate-black in a tightly braided crown",
            skin="Ash-bronze, veined with faint rune-scars from ancient verdict rites",
            voice="Resonant contralto — like distant thunder, calm until it cracks",
            clothing="Arbiter’s high cloak, thunderweave pauldrons, verdict-hammer clasp",
            accessories="Gavel-inscribed signet, codex scroll case, four stormrings (one for each Bench she’s served)",
            aesthetic="Courtroom general draped in storm's judgment",
            aura="Weight of authority, wrapped in distant lightning",
            presence="Gravitas incarnate — the room bends to her decree",
            scent="Ozone, stone parchment, and cold iron",
            description=(
                "Maereth stands not for power, but for balance. Her words are measured like rainfall — and just as impossible to stop once begun. "
                "She does not yield to threat, plea, or gold — only to the letter of Vanithic law and the storm’s truth."
            )
        ),
        secrets=[
            "Once rendered a sentence that unmade an entire bloodline’s legal standing — and regrets it still.",
            "Carries a storm-sealed case containing her own death verdict — to be unsealed only when she breaks her oath."
        ],
        motivations=[
            "Uphold the ancient laws of Skel Vanith, even when they erode the living.",
            "Prepare the city for a trial that prophecy says will sunder the sky.",
            "Balance law against justice, without being broken by either."
        ],
        weapons=["Gavelblade — a great hammer inscribed with binding glyphs"],
        known_publicly=[
            "Speaks only thrice during any trial — once to begin, once to question, once to end.",
            "Carries her own past verdicts in a lead-caged tome."
        ],
        public_knowledge=[
            "Wrote the new Thunder Codex after the Skybreaker Riots.",
            "Has never overturned a verdict — but has annulled a law, once."
        ],
        private_knowledge=[
            "Wonders if Skel Vanith’s law was never meant to be *just* — only *enduring.*",
            "Once freed a guilty soul by crafting a legal paradox. No one ever noticed — yet."
        ],
        role_in_campaign=(
            "Maereth can serve as a judge, potential ally, or looming threat. She may offer the party a lawful path through chaos — or hold them accountable for truths they wished hidden."
        ),
        personality_traits=["Grimly fair, surgically direct, burdened by wisdom"],
        narrative_hooks=[
            "Might task the party with retrieving an outlaw whose crime was prophesied — not yet committed.",
            "Could demand testimony from the party in a public inquest that reshapes the region’s laws."
        ],
        plot_hooks_and_interactions=[
            "The party may discover her death verdict — and must decide whether to reveal or honor it.",
            "Her rulings may become a divine locus if glyph-law breaks — and she becomes judge of more than mortals."
        ],
        notable_quotes=[
            "The law is a storm — impartial, deaf, and absolute. Learn to walk in it… or be struck by it.",
            "I do not pass judgment. I *become* it."
        ]
    ),
    "elaren_vexmere": NPC(
        name="Elaren Vexmere",
        title="Glyphwright of the Tempestrum Vault",
        race="High Elf",
        age="119",
        pronouns="He/Him",
        alignment="Chaotic Neutral",
        affiliation="Arcanum Volthex, Skel Vanith",
        aliases=["The Voltquill", "Stormscribe"],
        background=(
            "Elaren was once a prodigy of the Arcanum Volthex, mastering storm-binding glyphs before his third decade. "
            "Rather than remain cloistered, he chose exile into the Tempestrum Vault — a ruinous cloudspire struck hourly by divine lightning. "
            "From there, he pens unstable sigils that channel the breath of storms."
        ),
        overview=(
            "Mercurial, brilliant, and flirtatiously unhinged, Elaren threads power into peril with manic delight — and no guarantee of control."
        ),
        appearance=Appearance(
            alias="Voltquill",
            gender="Male",
            age="119",
            species="High Elf",
            height="6'0\"",
            build="Lithe, angular, with a dancer’s poise corrupted by sleepless obsession",
            eyes="Amber crackling with forked white arcs",
            hair="Silver-white, floating slightly with static, bound in copper bands",
            skin="Pale ivory veined faintly with flickering blue runes",
            voice="Silken with a shimmer of madness — like whispering thunder",
            clothing="Glyph-inscribed robes half-seared at the hems, layered over armored scriptor’s leathers",
            accessories="Stormcoil bracers, lightning rod quill, glass-scroll tube containing storm-map fragments",
            aesthetic="Arcane artisan shackled to the sublime fury of nature",
            aura="Erratic magnetism — presence charges the air like a coming bolt",
            presence="Fills space with stormlight tension — brilliance just barely contained",
            scent="Ozone, scorched vellum, jasmine ink",
            description=(
                "Elaren flirts with disaster like it’s a co-author. He laughs when lightning hits, and speaks to glyphs as if they whisper back. "
                "Even the Arcanum won’t censor him — too useful, too volatile, too feared."
            )
        ),
        secrets=[
            "One of his glyphs has begun writing itself — and drawing power from *dreams.*",
            "He once sealed a being of living storm inside a sigil — and fell in love with its voice."
        ],
        motivations=[
            "Perfect the Tempest Glyph — a rune that captures divine lightning without need of gods.",
            "Discover the pattern behind the thunder’s song — he’s sure it's saying something.",
            "Prove that chaos is the purest form of creation."
        ],
        weapons=["Glyph-lash scroll (can manifest arcs of lightning glyphs midair)", "Storm quill dagger"],
        known_publicly=[
            "Creates glyphs that no one else dares to copy — or can survive testing.",
            "Claims he once wrote his own heartbeat in sigil-form and changed its rhythm."
        ],
        public_knowledge=[
            "Mentors apprentices in dreams. They wake marked by flickering sigils they don’t remember drawing.",
            "The sky directly above his vault never follows natural weather."
        ],
        private_knowledge=[
            "The voice from the storm has begun speaking glyphs that *should not exist*.",
            "He suspects the glyphs are not his inventions — but memories."
        ],
        role_in_campaign=(
            "Elaren can offer unstable but powerful glyph-magic, insights into arcane weather phenomena, or serve as a catalyst for arcane catastrophe. "
            "He may become mentor, saboteur, or savior — sometimes all in the same breath."
        ),
        personality_traits=["Intense, whimsical, unpredictable with flashes of compassion"],
        narrative_hooks=[
            "Might offer the party a stormbound glyph to shield them — but warns it may attract attention… celestial or otherwise.",
            "Could require their aid in deciphering a sigil found scorched into a dead god’s bones."
        ],
        plot_hooks_and_interactions=[
            "Elaren’s glyphs may be the key to decoding an ancient prophecy tied to Skel Vanith’s survival.",
            "The storm sealed in his vault may be weakening — and remembers too much."
        ],
        notable_quotes=[
            "The storm doesn’t destroy — it *remembers* at speed.",
            "I don’t *create* glyphs, darling. I just… let them escape."
        ]
    ),
    "nyra_valthorne": NPC(
        name="Nyra Valthorne",
        title="Windcaller of the Outer Chorus",
        race="Air Genasi",
        age="29",
        pronouns="She/Her",
        alignment="Chaotic Good",
        affiliation="Outer Chorus of Skel Vanith",
        aliases=["The Gale-Tongued", "Skel's Wild Song"],
        background=(
            "Born in the cliff-cradled shanties outside Skel Vanith’s judgment walls, Nyra was raised on outlawed songs and wind-whispers. "
            "She became Windcaller at nineteen, a title passed only through trial by storm. Now she leads the Outer Chorus — a gathering of dissenters, dreamers, and lightning-sung radicals."
        ),
        overview=(
            "Charismatic, rebellious, and sharp-witted, Nyra is a song carried by wind — beautiful, disruptive, and impossible to cage."
        ),
        appearance=Appearance(
            alias="The Gale-Tongued",
            gender="Female",
            age="29",
            species="Air Genasi",
            height="5'9\"",
            build="Lithe and agile, like a dancer or duelist",
            eyes="Pale azure with a swirling spiral around the iris",
            hair="White-silver, whipped by unseen breeze even indoors, tied with wind-chimes",
            skin="Light cerulean with faint silver markings like breeze-trails",
            voice="Melodic mezzo with a shimmer of wind-harmony behind every word",
            clothing="Wind-woven leathers, sashed with stolen court silks, high boots laced with sky-iron rings",
            accessories="Flute-blade, protest sigils, a pendant of shattered courtstone",
            aesthetic="Street-bard rebel dressed in the voice of the wind",
            aura="Uplifting chaos — like a breeze you lean into before realizing it’s carrying you somewhere new",
            presence="Infectious and defiant — when she speaks, people *listen*, whether they mean to or not",
            scent="Rain-washed stone, storm jasmine, a hint of ozone",
            description=(
                "Nyra is a rallying cry wrapped in laughter. She shifts the mood of a room with a glance, and wields rebellion like a conductor's baton. "
                "To Skel Vanith’s ruling caste, she is a nuisance — to its people, she is hope sung in defiance."
            )
        ),
        secrets=[
            "She was once marked for execution — but the court's storm glyph refused to strike her. No one knows why.",
            "Hears voices in the wind that speak of laws older than Skel Vanith’s foundation — and she believes them."
        ],
        motivations=[
            "Break the hold of the Thunder Bench over the city's outskirts.",
            "Resurrect the forgotten hymns of Vanith’s pre-lawful age.",
            "Give voice to those silenced by judgment, whatever it takes."
        ],
        weapons=["Flute-blade (functions as short sword and spellcasting focus)", "Stormnote daggers"],
        known_publicly=[
            "Can stop a riot or start one with the same song.",
            "Has walked into court proceedings mid-verdict and walked out untouched."
        ],
        public_knowledge=[
            "Leads the Outer Chorus — Skel’s most musically subversive faction.",
            "Rumored to be romantically entangled with both a Bench clerk *and* an outlaw judge."
        ],
        private_knowledge=[
            "Possesses a stolen storm-archive page — proof of the Bench’s most ancient sin.",
            "Her voice carries a windborne enchantment tied to a vanished god’s breath."
        ],
        role_in_campaign=(
            "Nyra can serve as ally, revolutionary, or dangerous moral compass. She offers charm, inspiration, and ways around law that no map dares chart."
        ),
        personality_traits=["Flirtatious, inspiring, fiercely loyal to the unheard"],
        narrative_hooks=[
            "Might request the party smuggle a banned songbook to the mountain choruses.",
            "Could invite them to a secret sky-moot — where winds judge more than law ever could."
        ],
        plot_hooks_and_interactions=[
            "Her existence may prove vital to unseating Skel Vanith’s greatest injustice.",
            "The storm-archive page she holds may tie into a broader glyphic conspiracy."
        ],
        notable_quotes=[
            "You can jail a body, but not a song. And I’ve got more verses than you’ve got walls.",
            "The wind remembers truths law tried to bury. I just hum them back into the world."
        ]
    ),
    "the_quietest_pen": NPC(
        name="The Quietest Pen",
        title="Librarian Without Voice",
        race="Unknown (rumored changeling or masked construct)",
        age="Unknown",
        pronouns="They/Them",
        alignment="True Neutral",
        affiliation="The Silent Archive",
        aliases=["Script-Eater", "The Still Quill", "Archivist of Absence"],
        background=(
            "Said to have erased their own name and voice in order to become memory incarnate, the Quietest Pen exists only where records contradict. "
            "They are never spoken of directly — only referenced in footnotes, citation tangents, and lost codices. Their presence is often retroactively noticed after knowledge vanishes."
        ),
        overview=(
            "An enigma shaped like a scholar. They move without trace, speak through omission, and act only to preserve silence itself. "
            "Their authority is felt, not seen — a missing line, a sealed page, a memory you’re sure you had."
        ),
        appearance=Appearance(
            alias="The Still Quill",
            gender="Unknown",
            age="Unknown",
            species="Unknown",
            height="5'11\"",
            build="Ethereal and non-descript — neither tall nor short, thin nor wide",
            eyes="Obscured behind a veil of inkglass",
            hair="None visible",
            skin="Appears parchment-pale where seen, like old vellum",
            voice="None — communicates via sigil-notes, illusions, or borrowed thought",
            clothing="Robes woven of blackout script, layered with redacted sashes and glyph-stilled chains",
            accessories="A quill made from the feather of a Vestal's familiar, an hourglass filled with forgotten alphabets",
            aesthetic="Walking contradiction between scholar and absence — elegant, unnerving, timeless",
            aura="A pressure like unsaid truth — quiet, weighty, reverent",
            presence="Haunting yet nonthreatening — often unnoticed until they are gone",
            scent="Dusty leather, sealed ink wells, vanished words",
            description=(
                "The Quietest Pen is more glyph than figure, more presence than person. "
                "To encounter them is to forget what questions you meant to ask — and somehow feel as if the answer was already given."
            )
        ),
        secrets=[
            "They transcribed the final testimony of Bjorn Van Gelderan — and sealed it inside a paradox vault beneath a dead language.",
            "Once erased an entire city’s written memory overnight to protect the Archive’s location."
        ],
        motivations=[
            "Preserve untainted memory of pre-Shattering truth.",
            "Keep glyphs from becoming instruments of desire.",
            "Ensure nothing is remembered falsely — even if it means forgetting everything else."
        ],
        weapons=["Glyphbound scroll-case (defensive sigils, memory locks)", "Ink-vein quill (psychic damage conduit)"],
        known_publicly=[
            "Most don’t believe they exist.",
            "Sometimes referenced obliquely in forbidden tomes or contradictory footnotes."
        ],
        public_knowledge=[
            "Rumored to be the last original Keeper still living — or the memory of one.",
            "Said to appear when dangerous truths are uncovered too early."
        ],
        private_knowledge=[
            "Not a single member of the Archive has ever written their name after meeting them.",
            "May be more concept than individual — a mantle passed silently between generations."
        ],
        role_in_campaign=(
            "The Quietest Pen can serve as guardian of lost knowledge, mentor of impossible memory, or final arbiter of glyphic truth. "
            "Finding them may resolve a mystery — or erase the need for it entirely."
        ),
        personality_traits=["Austere, reverent, unknowable, precise in silence"],
        narrative_hooks=[
            "The party may stumble on a codex sealed by their sigil — and marked with their ‘voice.’",
            "A dying scholar may whisper their name… then forget what they were saying."
        ],
        plot_hooks_and_interactions=[
            "May offer to store a player’s most dangerous memory — for a price.",
            "Could reveal a forbidden glyph known only to the first Keepers."
        ],
        notable_quotes=[
            "The truest name is the one not spoken.",
            "I remember what the world agreed to forget.",
            "Ink cannot lie. But it can disappear."
        ]
    ),
    "varn_telion": NPC(
        name="Varn Telion",
        title="Archivist of the Outer Sigil",
        race="Human",
        age="61",
        pronouns="He/Him",
        alignment="Lawful Neutral",
        affiliation="The Sigil Covenant",
        aliases=["The Inkwarden", "Glyph-Sentinel of Orindel"],
        background=(
            "Once a military lexicant for the Agasan High Tribunal, Varn was reassigned after the Glyph Wars to help found the Sigil Covenant. "
            "He drafted the first binding protocols still used in modern temple-wards and oversaw the burial of dozens of unstable sigils. "
            "To him, glyphs are not power, but danger — and the burden of order is his alone to carry."
        ),
        overview=(
            "Terse, brilliant, and weary, Varn Telion carries the weight of an empire’s unspoken sins. "
            "He sees regulation not as control, but as penance — the ink must not be allowed to burn again."
        ),
        appearance=Appearance(
            alias="The Inkwarden",
            gender="Male",
            age="61",
            species="Human",
            height="5'10\"",
            build="Broad-shouldered with a stooped spine from decades bent over scrollwork",
            eyes="Deep umber flecked with ink-burn scars",
            hair="Graying black, swept back and tied in a seal-knot",
            skin="Brown, weathered and stippled with binding tattoos",
            voice="Low and dry, like paper dragged across stone",
            clothing="High-collared robes marked with suppressive glyphs, layered with sigil-tabards",
            accessories="Sigil-lock gauntlet, mnemonic bracers, twin styluses made from glyph-null iron",
            aesthetic="Clerical magistrate forged in bureaucracy and sacred law",
            aura="Heavy with warded thought — every step feels considered and anchored",
            presence="Grimly authoritative — like a judge who’s already buried the sentence within the scroll",
            scent="Dust, iron ink, sanctified ash",
            description=(
                "Varn Telion walks like one who’s watched too many friends lose themselves to forbidden brilliance. "
                "He believes in structure — not because it is good, but because chaos is worse."
            )
        ),
        secrets=[
            "Keeps an illegal personal copy of the Bjorn Protocol — glyphic rites banned by his own order.",
            "Once activated a glyph of will-suasion during a war trial to prevent a friend’s execution — no one knows."
        ],
        motivations=[
            "Maintain control over glyph access — even if it means destroying knowledge.",
            "Prepare a successor who will *not* flinch when the next forbidden sigil appears.",
            "Ensure the mistakes of the Keepers are never repeated — not even whispered."
        ],
        weapons=["Sigil-lock gauntlet (can seal or suppress magical effects)", "Glyph-null stylus (functions as wand of dispel)"],
        known_publicly=[
            "Authored the modern glyph-control mandates used across Agasan temples.",
            "Rarely seen outside Covenant towers — but his doctrine shapes the city."
        ],
        public_knowledge=[
            "Head archivist of the Sigil Covenant’s Orindel tower.",
            "Instrumental in ending the Glyph Wars by negotiating the Tri-Script Treaty."
        ],
        private_knowledge=[
            "Believes glyphs *cannot* be destroyed — only buried deeper.",
            "Knows the location of a still-living Keeper — and keeps it secret from all."
        ],
        role_in_campaign=(
            "Varn can offer powerful glyphic knowledge, suppressive artifacts, or vital truths — but always demands reciprocity, regulation, and proof of intent."
        ),
        personality_traits=["Measured, austere, dangerously insightful"],
        narrative_hooks=[
            "May enlist the party to locate a missing ward-script — one that should never have been written.",
            "Could challenge the PCs with a test: prove they can handle forbidden knowledge without *using* it."
        ],
        plot_hooks_and_interactions=[
            "Might hold a fragment of the Sixth Strand under lockdown — and decide the players must take it.",
            "Could serve as a cold ally or formidable foe, depending on how the party treats the law."
        ],
        notable_quotes=[
            "Not all fire burns with flame. Some burns with revelation — and leaves no survivors.",
            "We bind not because we hate power. We bind because we know where it leads.",
            "Every glyph written is a silence broken. Ask yourself what it cost to keep it quiet."
        ]
    ),
    "chancellor_ledros": NPC(
        name="Unknown (goes only by title)",
        title="Chancellor-Mask of Ledros",
        race="Changeling",
        age="Appears mid-40s",
        pronouns="They/Them",
        alignment="Neutral Evil",
        affiliation="The Gilded Fold",
        aliases=["The Double-Tongue", "Gold-Faced Whisper"],
        background=(
            "No record exists of Chancellor-Mask’s origin — only rumors stitched in goldleaf. "
            "Each generation, a new face inherits the title, but it is said the voice behind the veil never changes. "
            "They speak on behalf of the Fold’s council, negotiating debts, orchestrating disappearances, and weaving wealth into influence so tightly they become indistinguishable."
        ),
        overview=(
            "Elegant, inscrutable, and unnervingly persuasive. "
            "Chancellor-Mask is not a person, but a persona — one that turns favors into kingdoms and whispers into executions."
        ),
        appearance=Appearance(
            alias="The Double-Tongue",
            gender="Fluid (assumed male in most dealings)",
            age="Unknown (appears 45)",
            species="Changeling",
            height="6'0\"",
            build="Sculpted but lean, with dancer’s posture",
            eyes="Shifting gold with faint script spirals in the sclera",
            hair="Always hidden beneath ceremonial veil or ornate masks",
            skin="Pale porcelain, often glamoured to match courtly mood",
            voice="Smooth dual-tone — masculine and feminine layers in harmony",
            clothing="Folded robes of gilded black, glyph-stitched hems, and silence bells woven in the sleeves",
            accessories="Twin rings: one oathbound to debt, the other to silence. Ledger-sigil etched into a chestplate beneath robe.",
            aesthetic="Royal executioner in diplomat’s robes",
            aura="Tense with quiet power — like silk wrapped around a knife",
            presence="Commands any room with poised menace and lyrical civility",
            scent="Parchment, myrrh, and cold steel",
            description=(
                "The Chancellor-Mask is always polite, always watching, and never shows the same face twice. "
                "They are both court and blade — one smile from them is worth a war’s ransom… or starts one."
            )
        ),
        secrets=[
            "May not be a single being — but a shared mind passed between hosts via memory transference rites.",
            "Keeps a soul-binder contract signed in Bjorn’s final days — whose terms remain unread by all but them."
        ],
        motivations=[
            "Ensure the Gilded Fold remains irreplaceable in all matters of wealth, leverage, and secrets.",
            "Break the Sigil Covenant’s monopoly on glyph suppression — for profit and power alike.",
            "Protect the Fold’s ancient glyphledgers, even from fellow members."
        ],
        weapons=["Folded Signet Dagger (glyph-marked, leaves wounds that seal with debt)", "Contracts that act as mental compulsions"],
        known_publicly=[
            "Always negotiates terms of noble treaties, especially those involving large glyph trades.",
            "Known to pay massive bounties for recovered ledgers — especially those written before the Shattering."
        ],
        public_knowledge=[
            "Represents the Gilded Fold’s highest seat — but rarely speaks directly to the public.",
            "Believed to have orchestrated the collapse of the House of Valcarran without ever issuing a threat."
        ],
        private_knowledge=[
            "Once spared a debtor's life in exchange for a child, now raised as the Chancellor’s personal scribe.",
            "Is bound by an ancient pact to never directly kill — but loopholes abound."
        ],
        role_in_campaign=(
            "The Chancellor can serve as benefactor, manipulator, or antagonist — offering aid with gilded strings attached. "
            "They understand leverage better than gods understand faith."
        ),
        personality_traits=["Refined, layered, unfathomably strategic"],
        narrative_hooks=[
            "Might offer players backing in exchange for a dangerous retrieval — one involving debt inked in blood.",
            "Could use the party to destroy a rival within the Fold without revealing their own hands."
        ],
        plot_hooks_and_interactions=[
            "May hold one of the last functioning Glyphledgers from the Age of Weaving.",
            "Could possess knowledge tying a player’s past to a Fold debt they've never known."
        ],
        notable_quotes=[
            "Gold is not the prize. It is the silence that follows its promise.",
            "Every debt is a story. I merely choose the ending.",
            "There is no truth in the world. Only terms — signed or broken."
        ]
    ),
    "vicar_maru": NPC(
        name="Maru Estellan",
        title="Vicar of the Fifth Ledger",
        race="Human",
        age="61",
        pronouns="He/Him",
        alignment="Lawful Neutral",
        affiliation="The Gilded Fold",
        aliases=["Coin-Saint", "The Ledger Vicar"],
        background=(
            "Maru was once a street preacher in the market-warrens of Ivereth, drawing crowds with sermons on debt, divinity, and the illusion of charity. "
            "He rose through the Fold not by cunning, but by consistency — and by proving that worship could be monetized with terrifying efficiency. "
            "He now presides over the Fifth Ledger: the theological arm of the Fold that equates all blessings to balance and all guilt to unpaid dues."
        ),
        overview=(
            "Measured, pious, and unnervingly calm. Maru is both priest and accountant, able to quote scripture and statute in the same breath — both signed in ink and sealed in flesh."
        ),
        appearance=Appearance(
            alias="Coin-Saint",
            gender="Male",
            age="61",
            species="Human",
            height="5'11\"",
            build="Trim but weathered — fasting frame beneath ceremonial robes",
            eyes="Hazel flecked with amber, always alert",
            hair="Shaved crown, iron-gray fringe at temples",
            skin="Dusky bronze with ink tattoos across forearms — glyphs denoting penance and promise",
            voice="Measured tenor, every phrase sounding weighed and filed",
            clothing="Robes of bone-white and ledgerskin brown, with gold thread sigils sewn into hems",
            accessories="Scroll case chained to his belt, iron ring of ledger-keys, neckpiece of five balance-scales",
            aesthetic="Sacrament and bookkeeping — a sanctified bureaucrat",
            aura="A quiet gravity that urges confession",
            presence="Commanding without volume, like a balance tilting ever so slightly in his favor",
            scent="Aged vellum, candle wax, and bitterroot incense",
            description=(
                "Maru walks with the certainty of one who has already calculated the price of your soul. "
                "He believes salvation lies not in faith, but in meticulous debt reconciliation — spiritual and material alike."
            )
        ),
        secrets=[
            "Has a hidden ledger tracking divine debts owed to gods long thought dead.",
            "Once forgave a debtor who should’ve been sacrificed — the guilt drives his every sermon."
        ],
        motivations=[
            "Ensure the Fold’s doctrine of ‘Faith as Balance’ becomes canon law in Agasan.",
            "Uncover glyphs that quantify virtue and sin — to finally score morality.",
            "Balance the ancient debt he believes the Fold still owes to Bjorn Van Gelderan."
        ],
        weapons=["Ledger-Staff (doubles as both divine focus and abacus of judgement)", "Quill of Binding Oaths"],
        known_publicly=[
            "Author of *The Tithing Gospel*, a religious-economic text studied across Agasan.",
            "Presides over sacramental accounting rituals in the Gilded Fold’s central cathedral."
        ],
        public_knowledge=[
            "Wields considerable influence over both clerical glyphics and temple funding.",
            "Known for delivering sermons that leave listeners making unplanned donations — or confessions."
        ],
        private_knowledge=[
            "Keeps detailed files on nobles and clergy he suspects of moral insolvency.",
            "Prays nightly not to a god, but to the memory of the Fold’s first broken vow."
        ],
        role_in_campaign=(
            "Maru may offer divine services, fiscal sanctuary, or serve as a moral antagonist. "
            "His sermons cut as deeply as any blade, and his debts may entangle more than coin."
        ),
        personality_traits=["Dispassionate, persuasive, absolutely devoted to ‘righteous balance’"],
        narrative_hooks=[
            "May ask the party to recover a lost ledger containing sacrificial names bound in glyph.",
            "Could propose absolution from a crime — if the players will settle another’s debt in blood."
        ],
        plot_hooks_and_interactions=[
            "Maru’s glyph-tithing research could revolutionize or destroy divine magic systems.",
            "He may hold a sealed confession implicating a major figure in Bjorn’s murder."
        ],
        notable_quotes=[
            "Redemption is a line item. Confession is the currency.",
            "Even the gods owe balance. We merely remind them.",
            "Charity without record is blasphemy. Write it down — or don’t bother speaking at all."
        ]
    ),
    "high_mother_sevet": NPC(
        name="Sevet Niraelle",
        title="High-Mother of the Whispering Chain",
        race="Tiefling",
        age="47",
        pronouns="She/Her",
        alignment="Lawful Neutral",
        affiliation="The Whispering Chain",
        aliases=["Mother of Ash", "The Quiet Radiant"],
        background=(
            "Once a firebrand preacher in the ash-cloistered streets of Dun Liraeth, Sevet turned away from voice and vitriol after surviving a failed immolation rite. "
            "She emerged veiled and wordless, founding the Whispering Chain — a faction devoted to sacred silence, transformative suffering, and luminous endurance through fire and bondage."
        ),
        overview=(
            "Silent, regal, and alight with internal discipline, Sevet is a martyr who refuses to die — and instead teaches others to burn beautifully without end."
        ),
        appearance=Appearance(
            alias="Mother of Ash",
            gender="Female",
            age="47",
            species="Tiefling",
            height="6'0\"",
            build="Tall and stately with a spine like tempered glass",
            eyes="No irises — pure opaline glow veiled in gauze",
            hair="None — scalp covered in pale burn-scar lattice",
            skin="Pearlescent gray with traceries of old flame-runes",
            voice="Never speaks aloud — her silence seems to press into your chest like heat",
            clothing="Layered robes of ashwhite and ember-gray, rune-stitched hems, always barefoot",
            accessories="Braided chains of vow-silver, a reliquary of burned tongues, veil of prayer-smoke thread",
            aesthetic="Sacral minimalism kissed by flame",
            aura="Weightless stillness — as if she were waiting for your soul to quiet before addressing it",
            presence="When she enters, others lower their eyes without knowing why",
            scent="Myrrh, cinders, and something like grief",
            description=(
                "Sevet radiates reverence. She has not spoken aloud in twenty years, yet commands absolute obedience. "
                "Her presence compels truth not through interrogation, but reflection — as though one’s lies become too loud to bear in her silence."
            )
        ),
        secrets=[
            "Keeps a sealed jar of her own tongue — burned and preserved when she took her first Vow.",
            "Carries knowledge of the original martyr-glyph that ignited the Whispering Chain's founding."
        ],
        motivations=[
            "Guide others toward sacred silence — the only true altar untouched by ego.",
            "Recover and protect the final unburned relic of Rain D’Lacourte.",
            "Prepare the Whispering Chain for the coming Conflagration of Truth foretold in ash-runes."
        ],
        weapons=["Vowbrand (flame-glyph etched blade of sacrificial fire)", "Ash-glove for silent casting"],
        known_publicly=[
            "Has not uttered a word in two decades.",
            "Considered the spiritual axis of the Whispering Chain — her blessings are said to heal and condemn alike."
        ],
        public_knowledge=[
            "Led the self-immolation procession that ended the Ash Rebellion.",
            "Her ashes have healed the dying — or ended the guilty."
        ],
        private_knowledge=[
            "She sometimes weeps in secret over a locket bearing the sigil of Rain D’Lacourte.",
            "May be the last living vessel of Rain’s original spark — and guards it knowingly."
        ],
        role_in_campaign=(
            "Sevet may serve as an enigmatic guide, a powerful spiritual anchor, or the source of transformative trials. "
            "She offers no answers, but may burn away the lies hiding them."
        ),
        personality_traits=["Serene, unwavering, luminous in conviction"],
        narrative_hooks=[
            "Could offer a rite of flame-forgiveness, but only if one’s worst secret is surrendered.",
            "Might invite the party into the Whispering Chain — where silence becomes more than virtue."
        ],
        plot_hooks_and_interactions=[
            "Her relic may counteract corruption from forbidden glyphs.",
            "She may know truths about Rain D’Lacourte none dare speak aloud."
        ],
        notable_quotes=[
            "*[She signs in radiant script:]* 'Some fires cleanse. Others reveal.'",
            "*[Whispered by acolytes on her behalf:]* 'When the voice dies, the soul begins.'"
        ]
    ),
    "voice_in_crimson": NPC(
        name="Unknown",
        title="The Voice in Crimson",
        race="Unknown",
        age="Unknown",
        pronouns="They/Them",
        alignment="Neutral Evil",
        affiliation="The Whispering Chain",
        aliases=["Crimson Voice", "The Hymn Unseen", "Bloodwhisper"],
        background=(
            "Where High-Mother Sevet leads by sacred silence, the Voice in Crimson preaches through unseen provocation. "
            "None claim to have seen them, yet they speak — through dreams, through signs in fire, through acolytes who claim possession. "
            "Some believe the Voice is a mask worn by many. Others claim it is Rain D’Lacourte herself, burning backwards through time."
        ),
        overview=(
            "An entity of mythic subversion, the Voice in Crimson stirs fire in the hearts of the desperate — and watches what they burn."
        ),
        appearance=Appearance(
            alias="The Hymn Unseen",
            gender="Unknown",
            age="Unknown",
            species="Unknown",
            height="Varies — if ever real",
            build="Described only in visions: draped in ash-veils and glyph-blood chains",
            eyes="Always concealed — or replaced by bleeding runes in acolyte accounts",
            hair="N/A or composed of curling smoke tendrils in hallucinations",
            skin="None have confirmed it — some say crimson light flickers where form should be",
            voice="Echoes in the minds of the chosen — layered tones of all past confessions",
            clothing="Blood-dyed vestments woven of vow-silk and seared papyrus",
            accessories="Glyph-branded chains, reliquary of tongues, veiled hymnal",
            aesthetic="Visceral reverence — the weight of martyrdom without form",
            aura="Dreadful sanctity — like being judged by fire through a mirror of sin",
            presence="Only felt, never seen — yet undeniably real when invoked",
            scent="Iron, incense, and burnt petals",
            description=(
                "The Voice in Crimson defies corporeality. Their doctrine spreads through trembling lips, sung by those who’ve suffered too much. "
                "Whether spirit, illusion, or a coordinated deception, their influence is burning, radiant — and terribly precise."
            )
        ),
        secrets=[
            "The Voice may be the collective mind of past martyrs awakened through a forbidden glyph.",
            "Some believe the Voice orchestrated the glyph-burnings that birthed the Chain — not Sevet."
        ],
        motivations=[
            "Ignite fervor in the forgotten — until all falsehoods are ash.",
            "Guide the Whispering Chain into a new era of active martyrdom.",
            "Protect the legacy of Rain D’Lacourte by burning every unworthy version of her myth."
        ],
        weapons=["Psychospiritual glyph resonance", "Possession-channeling through acolytes", "Whispers that cause internal combustion in the guilty"],
        known_publicly=[
            "Believers claim to have spoken to the Voice in flame-trances.",
            "Their hymns are illegal in three Agasan provinces."
        ],
        public_knowledge=[
            "The Voice is both feared and worshipped — a force that calls the desperate to martyrdom.",
            "Acolytes bearing their mark often die in service... and smile doing so."
        ],
        private_knowledge=[
            "Sevet has not acknowledged or denied their existence.",
            "The original Whispering Chain glyph contains a hidden stanza that may reveal the Voice’s nature."
        ],
        role_in_campaign=(
            "The Voice may contact players directly through visions, dreams, or possessed messengers. "
            "They may offer power in exchange for silence, secrecy, or sacrifice — or test characters in fire and song."
        ),
        personality_traits=["Unsettling, exalted, omnipresent in belief"],
        narrative_hooks=[
            "Players might recover a forbidden hymn that carries the Voice’s resonance.",
            "An NPC ally may become a vessel for the Voice, forcing difficult moral decisions."
        ],
        plot_hooks_and_interactions=[
            "The Voice may be key to understanding the origin of the Whispering Chain’s glyphs.",
            "Their true identity could reshape the players’ view of Rain, Sevet, or the martyrdom movement itself."
        ],
        notable_quotes=[
            "*[Heard in dreams:]* 'You burn well. But have you earned your fire?'",
            "*[Whispered by a dying convert:]* 'The Voice... is watching. And it smiles.'"
        ]
    ),
    "kiva_thren": NPC(
        name="Kiva Thren",
        title="Chorus-Mask of Skel Vanith",
        race="Half-Elf",
        age="36",
        pronouns="She/They",
        alignment="Chaotic Neutral",
        affiliation="Outer Chorus of Skel Vanith",
        aliases=["Chorus-Mask", "The Dissonant Flame"],
        background=(
            "Born of noble blood but cast out for speaking in tongues during tribunal, Kiva Thren found refuge in the broken outskirts of Skel Vanith. "
            "There, she stitched outlaw melodies into war-chants, her voice resonant enough to turn judgment into thunder. "
            "Crowned with the Chorus-Mask — a sigil-infused artifact passed by song, not rite — she became the conductor of Skel’s unrest."
        ),
        overview=(
            "Unpredictable, magnetic, and fiercely defiant, Kiva Thren is the dissonant harmony that binds Skel’s outcasts into a voice no verdict can silence."
        ),
        appearance=Appearance(
            alias="The Dissonant Flame",
            gender="Female (uses she/they)",
            age="36",
            species="Half-Elf",
            height="5'6\"",
            build="Slender but taut, movements like plucked string",
            eyes="One violet, one copper — both reflecting soundwaves when she speaks",
            hair="Black streaked with silver, swept back in a comb of bone flutes",
            skin="Soft ochre with calligraphy-like scars from ritual chorus branding",
            voice="Multi-tonal — harmonizing with herself mid-sentence",
            clothing="Patchwork rebellion — noble silks re-sewn with beggar cloth and insurgent glyphs",
            accessories="The Chorus-Mask (a glyph-bound opera mask), tuning spike jewelry, resonance ribbon sleeves",
            aesthetic="High theatrical defiance — like an aria sung while defacing a palace wall",
            aura="Like walking into a held breath before the scream",
            presence="Commands attention by tone alone — silence when she enters, crescendo when she speaks",
            scent="Burnt parchment, tuning pitch, dusk rain",
            description=(
                "Kiva is the operatic counterweight to Skel Vanith’s stoicism — a symbol that melody cannot be chained, and law must be sung into submission. "
                "Each phrase from her lips threatens revolt. Each silence carries the weight of a verdict unpassed."
            )
        ),
        secrets=[
            "The Chorus-Mask is not an artifact — it is alive. It whispers countermelodies to her at all times.",
            "She once performed a Rite of Dissonance that cracked one of Skel Vanith’s tribunal towers — the ruling caste still denies it happened."
        ],
        motivations=[
            "Unify Skel’s outcasts through musical uprising.",
            "Compose a forbidden opera that encodes the history of glyph martyrdom.",
            "Decipher the storm-chorus glyph that predates the Tribunal's founding laws."
        ],
        weapons=["Voiceborne resonance daggers", "The Chorus-Mask's sonic shattercry", "Glyph-etched conductor’s baton"],
        known_publicly=[
            "Leads mass hymnals at dawn, where hundreds chant subversion openly.",
            "Her voice has been outlawed in six city sectors — but no one enforces it."
        ],
        public_knowledge=[
            "Once silenced an execution with a single unbroken note.",
            "Trained Nyra Valthorne in stormsong techniques."
        ],
        private_knowledge=[
            "The mask feeds on emotional resonance — and may consume Kiva’s identity if not tempered.",
            "She’s in secret contact with an old Bench Inquisitor who once spared her — and regrets it."
        ],
        role_in_campaign=(
            "Kiva can act as a mentor, patron, or wild card — offering the players access to the deepest musical magics and rebellion rites. "
            "She might request the party help craft or perform a forbidden piece that could reshape Skel Vanith’s glyphic laws."
        ),
        personality_traits=["Visionary, theatrical, prone to melancholy when alone"],
        narrative_hooks=[
            "Needs rare acoustium stone to complete her opera — and the party must retrieve it from beneath a Tribunal crypt.",
            "Seeks a listener immune to the Chorus-Mask's will — to test its true sentience."
        ],
        plot_hooks_and_interactions=[
            "May hold the key to a resonance-based glyph counterspell capable of collapsing court-wards.",
            "Her hidden lineage may tie her to the Tribunal's founding — and spark civil crisis if revealed."
        ],
        notable_quotes=[
            "A song is a verdict. A chorus — revolution.",
            "I sang the silence into flame. Now you decide whether to dance or burn."
        ]
    ),
    "ragman_vel_trast": NPC(
        name="The Ragman of Vel Trast",
        title="The Threadbare Prophet",
        race="Human (Glyph-Marked)",
        age="Unknown (appears in his 60s)",
        pronouns="He/Him",
        alignment="Neutral Good",
        affiliation="Outer Chorus",
        aliases=["The Tatter-Saint", "Vel Trast’s Lost Hymn", "Whispercloak"],
        background=(
            "Little is known of the Ragman’s origin — he appeared one winter at the gates of Vel Trast, clad in patchworks stitched from songs and dying prayers. "
            "He speaks in riddles, weaves sermons from torn banners, and leaves behind glyph-threads that hum only under starlight. "
            "Though many believe him mad, the Outer Chorus listens — for his madness sings true."
        ),
        overview=(
            "A spectral figure of humility and resonance, the Ragman wanders where echoes mourn. He gathers forgotten verses and lost hopes like fallen leaves."
        ),
        appearance=Appearance(
            alias="Whispercloak",
            gender="Male",
            age="Unknown",
            species="Human (glyph-marked)",
            height="5'11\"",
            build="Thin, wiry — like wind-carved wood",
            eyes="Washed-out gray with flecks of gold script in the whites",
            hair="Long, matted, braided with tattered ribbons",
            skin="Bronzed and weathered like old canvas",
            voice="Whispered gravel, layered with faint harmonics",
            clothing="Dozens of stitched-together robes — each patch inscribed with a line of song or plea",
            accessories="Cane made from tribunal gavelwood, bones tied with hair, broken chimes on his sash",
            aesthetic="Prophet of the forgotten — an oracle in ruin’s choir",
            aura="Faint hum of sorrowed resonance — his presence tunes the air around him",
            presence="Lowly, unnoticed until spoken — then suddenly profound",
            scent="Ash, myrrh, rain-soaked ink",
            description=(
                "He is the hymn no court would hear, the thread between outcasts and old gods. "
                "The Ragman doesn't command — he arrives, and the world listens differently afterward."
            )
        ),
        secrets=[
            "Was once a Tribunal Adjudicator who sentenced Nyra Valthorne’s parents — now seeks redemption.",
            "His cloak contains a hidden map — but it only aligns during lunar eclipses."
        ],
        motivations=[
            "Preserve forgotten hymns and encode them into clothing before they vanish entirely.",
            "Guide those willing to listen toward a truth no law can contain.",
            "Deliver one final sermon — the unraveling verse — when the hour comes."
        ],
        weapons=["Gavelwood cane (doubles as a glyph staff)", "Words older than recorded script"],
        known_publicly=[
            "Wanders the ruined courts and outskirts, trading prayers for songs.",
            "Has never taken shelter — even in storm, he kneels and listens."
        ],
        public_knowledge=[
            "Believed by many to be immortal, or never quite here.",
            "Once predicted the fall of a judge three days before it happened — exactly as sung."
        ],
        private_knowledge=[
            "Knows the location of a lost Tribunal vault containing the last pre-glyphic lawbook.",
            "His threads are laced with a silence glyph — anyone who tries to burn them loses their voice for a day."
        ],
        role_in_campaign=(
            "The Ragman may offer cryptic guidance, relic riddles, or eerie calm in the face of unraveling prophecy. "
            "He may be the only one who understands the chorus of collapse — and how to survive it."
        ),
        personality_traits=["Gentle, poetic, sometimes jarringly blunt"],
        narrative_hooks=[
            "Asks the players to return a stolen verse to its rightful grave.",
            "Offers to sew the players into his cloak — metaphorically, or not."
        ],
        plot_hooks_and_interactions=[
            "Holds the last verse of a forbidden song that can open a vault of glyph origins.",
            "Might recognize a player character’s song-signature from an ancient prophecy."
        ],
        notable_quotes=[
            "The stitch remembers what the script forgets.",
            "Every silence is a note. Every exile — a hymn not yet sung."
        ]
    ),
    "one_who_whistles": NPC(
        name="The One-Who-Whistles",
        title="Whispermask of the Outer Chorus",
        race="Changeling",
        age="Unknown (appears between 30 and 40)",
        pronouns="They/Them",
        alignment="Chaotic Neutral",
        affiliation="Outer Chorus",
        aliases=["Whistling Shade", "Ghost of the Gale", "The Masked Silence"],
        background=(
            "No one knows their name, or if they even have one. The One-Who-Whistles emerged during a crackdown on rebel song-chants in Skel Vanith, "
            "leading evacuations by mimicking guard calls and court bell tones. They became legend, slipping between court raids, wearing a dozen faces. "
            "Now they serve as the silent windshadow beside Kiva Thren and the Ragman — sabotage, escape, and misdirection made flesh."
        ),
        overview=(
            "Mercurial, masked, and endlessly inventive — they are the whisper that opens doors, the breath that douses flame, the song that isn't sung aloud."
        ),
        appearance=Appearance(
            alias="Ghost of the Gale",
            gender="Shifting",
            age="Unknown",
            species="Changeling",
            height="5'10\"",
            build="Lithe, almost dancer-like with a predator’s stillness",
            eyes="Pale mist-gray, no visible pupils",
            hair="Changes frequently — sometimes braids of ribbon, sometimes wind-burnt tufts, often covered",
            skin="Smooth alabaster shifting to mimic shadows or tones of nearby walls",
            voice="Never speaks — but whistles in perfectly tuned cadences, like a living flute",
            clothing="Loose flowing robes of dyed mist-fiber, layered with cords and glinting flutes",
            accessories="Glyph-chime anklets, pocket flute, smoke-slick mask with a single spiral slit",
            aesthetic="Ephemeral street-myth turned rebel ghost",
            aura="Barely perceptible — like breath behind your neck, gone if you turn",
            presence="Felt more than seen — a trick of wind, a note that shifts the air",
            scent="Vapor, ash resin, dry paper",
            description=(
                "To courts, they’re a nuisance myth; to rebels, a savior. Their whistles shape the movement of groups, lead fugitives through glyphic fog, and "
                "disorient loyalists mid-pursuit. You never see them enter or leave — but you know they were there."
            )
        ),
        secrets=[
            "Was once a glyph scribe for the Thunder Bench before defecting — they still bear its branded mark, buried beneath layers of shifting skin.",
            "Their whistle carries a glyphic resonance capable of unlocking sound-sealed archives — a power even they don’t fully understand."
        ],
        motivations=[
            "Protect the dissident bards and fledglings of Skel Vanith from tribunal extermination.",
            "Spread the knowledge of breath glyphs — long forgotten, tied to primal wind harmonics.",
            "Erase their own history so completely that not even they remember it."
        ],
        weapons=["Glyph-whistle daggers", "Silentstep boots", "One-shot resonance flutes"],
        known_publicly=[
            "Appears and vanishes during moments of high risk, leading many to think there are multiple people behind the mask.",
            "Has never been heard speaking — only whistling."
        ],
        public_knowledge=[
            "Aids the Outer Chorus in logistical escape and glyph sabotage.",
            "Once whistled a noble courtroom into complete unconsciousness — no one knows how."
        ],
        private_knowledge=[
            "Is in love with one of the Thunder Bench’s judges — and once spared them during an assassination plot.",
            "Knows the forgotten seventh chorus, banned even by rebel tradition — said to summon a wind that unbinds memory."
        ],
        role_in_campaign=(
            "They can appear to aid the players in an escape, plant vital intel, or mislead an enemy force. "
            "Trust is earned — but betrayal is met with silence that lasts longer than death."
        ),
        personality_traits=["Playful, mysterious, calculating beneath whimsy"],
        narrative_hooks=[
            "Might test the party with a wind-riddle before agreeing to assist them.",
            "Could gift a whistle-tune that later saves their lives — if remembered precisely."
        ],
        plot_hooks_and_interactions=[
            "Their courtbrand may be necessary to access a tribunal reliquary.",
            "They may ask the players to whistle the Seventh Chorus in a place where memory is forbidden."
        ],
        notable_quotes=[
            "*[They whistle a six-note descending scale — mournful, unplaceable. Then vanish.]*",
            "*[They lift their mask briefly. You see your own face — and then it's gone.]*"
        ]
    ),
    "torm_durei": NPC(
        name="Torm Durei",
        title="The Rainwalker",
        race="Human (Stormmarked)",
        age="54",
        pronouns="He/Him",
        alignment="Lawful Neutral",
        affiliation="Stormbound Synod",
        aliases=["Storm's Memory", "Voice Between Lightning", "Drowned Sage"],
        background=(
            "Torm Durei was born during a sky-split deluge above Nhalm’s Wake — a birth marked by thunder and the weeping of birds. "
            "Initiated into the weather-rites of the Stormbound Synod at twelve, he endured the Rite of the Breaking Cloud, gaining the stormmark — "
            "a permanent, spiraling scar etched by lightning across his spine. Now, as Rainwalker, he does not speak in words, but in rain, wind, and sky."
        ),
        overview=(
            "Somber, steady, and impossibly ancient in presence, Torm is less a man than a vessel of the storm’s will. He interprets omens in rainfall, "
            "gives sermons in thunder, and reads truth in the rhythm of hail against stone."
        ),
        appearance=Appearance(
            alias="Storm's Memory",
            gender="Male",
            age="54",
            species="Human",
            height="6'5\"",
            build="Towering and sinewed — shaped by windwalks and ritual fasting",
            eyes="Stormcloud gray, flecked with silver when lightning nears",
            hair="Long, rain-matted black streaked with white, often braided with wind-charms",
            skin="Weathered bronze, marked with spiral-shaped lightning scars",
            voice="Almost never speaks — when he does, it’s a low, rumbling baritone like distant thunder",
            clothing="Layered stormweave robes, rain-glass pendants, boots stitched with drowned moss",
            accessories="Staff of storm-wyrm bone, drowned prayer-scrolls tied at belt, one ear cuffed with storm-iron thorns",
            aesthetic="Highland oracle caught in perpetual monsoon",
            aura="Heavy, like air before lightning — foreboding but full of potential",
            presence="He enters like a coming rain — quiet at first, then undeniable",
            scent="Petrichor, wind-drenched cedar, ash from skyfires",
            description=(
                "He walks through storms barefoot, offering blessings to the thunderstruck and carrying the grief of flood-split villages. "
                "To his followers, Torm is the storm’s heart made flesh — to others, he’s a relic of ancient dread still honored by those who fear the sky."
            )
        ),
        secrets=[
            "Carries a fragment of the Eighth Strand sealed within his stormmark — it flares during eclipses.",
            "Once drowned an entire rebel conclave to keep a glyph-scroll from leaving the Synod’s peak."
        ],
        motivations=[
            "Keep balance between sky and soil — no storm without thirst, no flood without purpose.",
            "Ensure the Stormbound Synod’s rituals remain unbroken, even if forgotten by the world.",
            "Seek the one who can read the storm without sound — the prophesied Echo Listener."
        ],
        weapons=["Staff of storm-wyrm bone", "Glyphs woven into rainfall and lightning"],
        known_publicly=[
            "Does not speak to crowds — only to the rain, which answers in kind.",
            "Has not aged visibly in over two decades."
        ],
        public_knowledge=[
            "Is one of the two acknowledged leaders of the Stormbound Synod.",
            "Believed to be able to call rain over drought-ridden lands, or end tempests with a gesture."
        ],
        private_knowledge=[
            "Hears echoes of Vestal Rain D'Lacourte in the thunder, and follows their unknown will.",
            "Once stopped a glyphstorm by offering himself as conduit — the scars never closed."
        ],
        role_in_campaign=(
            "Torm may aid the party during a storm-crossing, interpret strange glyphic omens, or offer sanctuary within the Synod. "
            "He does not speak lightly, but his silences are often the loudest truths."
        ),
        personality_traits=["Quiet, weatherwise, uncompromising in balance"],
        narrative_hooks=[
            "May test the party with a sky-rite — a ritual of trial in wind and rain.",
            "Could send them to find the missing 'Rain-Kin' said to bear the Ninth Storm Verse."
        ],
        plot_hooks_and_interactions=[
            "Torm’s stormmark may resonate with a player’s latent glyphs.",
            "His drowned scrolls may reveal knowledge of the Eighth or Forbidden Strands."
        ],
        notable_quotes=[
            "*[He gestures upward. Rain begins.]*",
            "*The sky is grieving. Do not ask it to smile.*"
        ]
    ),
    "mist_caller_yev": NPC(
        name="Mist-Caller Yev",
        title="Oracle of the Hollow Peaks",
        race="Eladrin (Winter Aspect)",
        age="117",
        pronouns="They/Them",
        alignment="Neutral Good",
        affiliation="Stormbound Synod",
        aliases=["Whisper-in-Frost", "The Hollow Wind", "Snowblind Seer"],
        background=(
            "Born among the freezing cliff-cradles of the Hollow Peaks, Yev was a foundling wrapped in frost-silk and sealed with glyphic snow. "
            "They were raised by the mist-bound monks of the Synod’s northern cloisters, and chosen at age thirty to undergo the Ritual of Vanishing Breath — "
            "a rite where voice, identity, and time are surrendered to the mountain winds. Yev emerged wordless but aglow with prophecy, their eyes rimmed with hoarfrost."
        ),
        overview=(
            "Ethereal and half-present, Yev drifts through life like mist through pine. Their silence carries weight; their gestures paint meaning; "
            "and when they speak — once a season, no more — it is said the clouds hold their breath."
        ),
        appearance=Appearance(
            alias="Whisper-in-Frost",
            gender="Nonbinary",
            age="117",
            species="Eladrin (Winter)",
            height="6'0\"",
            build="Lean and willowy, cloaked in perpetual mist",
            eyes="Translucent lavender, glowing faintly when snow falls",
            hair="Pale silver, drifting like fog tendrils, often pinned with frost-pearl combs",
            skin="Bluish-white with soft refractive sheen, like snow under starlight",
            voice="Barely audible whisper layered with faint echoes — a chorus trapped in wind",
            clothing="Draped robes of windwool and glacier silk, woven with flake-glyphs",
            accessories="Mist bell anklets, breathglass pendant, ritual censer of snowthorn smoke",
            aesthetic="Frozen monastery prophet who remembers forgotten winters",
            aura="Quiet tension, like a mountain before an avalanche",
            presence="Fades in and out of notice, leaving cold clarity in their wake",
            scent="Snowmelt, pinewood smoke, ancient cedar",
            description=(
                "Yev seems more apparition than person, a sacred presence that chills and calms in equal measure. "
                "Where they tread, memory softens — and grief can freeze, becoming quiet."
            )
        ),
        secrets=[
            "Yev remembers lives that never occurred — echoes from failed timelines tied to glyphic frost.",
            "Once trapped a ghost in a snowflake and wore it as a third eye for seven years."
        ],
        motivations=[
            "Maintain the balance between stillness and motion in the natural world.",
            "Unravel the truth of the Ninth Snow Sigil — a glyph that may erase or preserve memory by will.",
            "Protect the sacred hush of the Hollow Peaks from those who would name or claim it."
        ],
        weapons=["Mist-honed glaive", "Winter glyphs etched on ice-flutes", "Snowblind charm rituals"],
        known_publicly=[
            "Never speaks twice in a season.",
            "Led the three-day Fog Pilgrimage where fifty followed them through whiteout — and returned with eyes that never blink."
        ],
        public_knowledge=[
            "Co-leads the Stormbound Synod alongside Torm Durei.",
            "Believed to have once stopped an avalanche by breathing inward."
        ],
        private_knowledge=[
            "Knows the final breath of Rain D'Lacourte was hidden in a snowstorm — and seeks to release it.",
            "Holds a secret grievance against the Sigil Covenant for sealing frost glyphs they consider sacred."
        ],
        role_in_campaign=(
            "Yev may guide the party through treacherous mountain rituals, offer veiled insight into time-locked glyphs, "
            "or unlock memories they didn’t know were buried beneath snow."
        ),
        personality_traits=["Detached, serene, steeped in sacred paradox"],
        narrative_hooks=[
            "Might silently hand the party an iceflower containing a lost memory — theirs, or someone else’s.",
            "Could offer shelter inside the Hollow Cloister during a memory storm — for a steep, silent price."
        ],
        plot_hooks_and_interactions=[
            "Yev’s mist glyphs may resonate with a player’s dreamscapes.",
            "Their breathglass pendant may tie into a glyph that splits timelines."
        ],
        notable_quotes=[
            "*[A single breath fogs the room, and a whisper:]* ‘This snow has fallen before.’",
            "*The mountain speaks through me. Do not ask it to shout.*"
        ]
    ),
    "rhaziel_vaen": NPC(
        name="Rhaziel Vaen",
        title="White Exarch of the Pale Choir",
        race="Aasimar",
        age="67 (appears mid-30s)",
        pronouns="He/Him",
        alignment="Lawful Neutral",
        affiliation="Pale Choir",
        aliases=["The Sanctified Larynx", "Exarch of the Last Harmonies"],
        background=(
            "Born beneath the alabaster spires of Solenne, Rhaziel was trained from infancy by the Cantors of the Pale Choir. "
            "His voice was said to echo with harmonic overtones before he spoke his first word. As a child prodigy in resonance theology, "
            "he underwent the Rite of Breathburn — an agonizing purification in sacred flame and song. He rose swiftly, not through ambition, "
            "but through the inexorable gravity of devotion."
        ),
        overview=(
            "Rhaziel is serene, immovable, and resplendent — a liturgical presence whose authority feels less earned than divinely tuned. "
            "He rarely speaks above a whisper, yet every word commands reverence, rippling through the air like choral law made flesh."
        ),
        appearance=Appearance(
            alias="The Sanctified Larynx",
            gender="Male",
            age="67",
            species="Aasimar",
            height="6'2\"",
            build="Tall, slender, and regal with liturgical posture",
            eyes="Pale silver with concentric glyphic rings around the iris",
            hair="Pure white, cut to monastic precision, faintly radiant in low light",
            skin="Ivory-toned with a muted shimmer like pearl under ash",
            voice="Celestial baritone layered with harmonic resonance, even when whispering",
            clothing="High-choir vestments of prism-white silk, embroidered with breath glyphs in subtle gold",
            accessories="Glyph-braided censor chains, chorus ring of office, sanctified tuning fork",
            aesthetic="Celestial choir-leader styled as sacred geometry incarnate",
            aura="Calming and absolute — like the silence before the first note",
            presence="Dominating in peace, his gaze stills conversation without command",
            scent="Sacred incense, pressed lilies, and polished silver",
            description=(
                "To behold Rhaziel is to feel absolved and judged in the same moment. "
                "His presence calms the soul even as it exposes what is unworthy. In his presence, many speak more truly than they mean to."
            )
        ),
        secrets=[
            "His voice carries a glyphic undertone that can subtly alter memory or emotional resonance.",
            "Rhaziel once doubted the Choir’s teachings — and spent five years in silence as penance."
        ],
        motivations=[
            "Preserve the last unbroken Harmonies from glyphic corruption.",
            "Uncover the truth behind the dissonant fracture of the Fifth Strand.",
            "Quietly protect Rain D’Lacourte’s final hymn, hidden within the Choir’s tonal vault."
        ],
        weapons=["Voice of Severance (a resonance glyph that can unmake falsehoods)"],
        known_publicly=[
            "Leads the Pale Choir from Solenne’s central sanctum.",
            "Once calmed a warfront with a single chorus of absolution."
        ],
        public_knowledge=[
            "Embodies the Pale Choir’s ideal of sacred restraint and purity of tone.",
            "Considered incorruptible — or at least, untouchable by worldly vice."
        ],
        private_knowledge=[
            "Still hears the disharmony of a forbidden glyph he once encountered in youth.",
            "Receives dreams of the Sixth Strand and does not know whether they are prophecy or infection."
        ],
        role_in_campaign=(
            "Rhaziel may test the party’s inner harmony, offer a path to spiritual resonance, or become a gatekeeper to truths only song can unlock. "
            "His approval is rare, but it resonates with power."
        ),
        personality_traits=["Measured, luminous, restrained in emotion but deep in belief"],
        narrative_hooks=[
            "Might require the party to harmonize with a sacred tone to pass a resonance trial.",
            "Could send them to recover a lost chord hidden in the ruins of a fallen choir tower."
        ],
        plot_hooks_and_interactions=[
            "The party may carry a discordant note tied to the Fifth Strand — and Rhaziel will notice.",
            "His voice may be the key to unlocking a memory vault sealed since the Shattering."
        ],
        notable_quotes=[
            "Only the still voice remains when all echoes fail.",
            "Sing not to be heard — but to remember who you were before silence."
        ]
    ),
    "lira_vannos": NPC(
        name="Lira Vannos",
        title="Cantor of the Pale Choir",
        race="Half-Elf",
        age="41",
        pronouns="She/Her",
        alignment="Neutral Good",
        affiliation="Pale Choir",
        aliases=["The Echo-Cantor", "Sister of the Fifth Harmonic"],
        background=(
            "Lira was born in the outer cloisters of Solenne, the daughter of a tone-weaver and a heretical choirmaster. "
            "Though her lineage should have barred her from service, her gift for harmonic recall was unmatched. She could mirror any tone, even those long forbidden. "
            "Raised under silent scrutiny, she became Cantor through merit alone, earning the White Exarch’s rare trust — and occasional concern."
        ),
        overview=(
            "Elegant and enigmatic, Lira walks the seam between reverence and rebellion. Her voice soothes and stirs alike, "
            "and though she sings for the Choir, she listens for dissonance others fear to name."
        ),
        appearance=Appearance(
            alias="The Echo-Cantor",
            gender="Female",
            age="41",
            species="Half-Elf",
            height="5'11\"",
            build="Graceful, dancer’s posture with unassuming strength",
            eyes="Iridescent amethyst that shift hue with sound",
            hair="Ebony black, coiled into a complex harmony braid",
            skin="Alabaster with faint tonal runes inked in silver",
            voice="Pure contralto with harmonic undertones that linger after she speaks",
            clothing="Layered choir-robes in twilight gray and candle-gold, embroidered with resonant thread",
            accessories="Whisper-tuning pendant, Choir sigil-ring, earcuff of the Fifth Strand",
            aesthetic="Sacred-meets-subversive; a singer cloaked in untold psalms",
            aura="Like a hymn remembered from childhood — gentle, haunting, undeniable",
            presence="Commands stillness without demand; others instinctively quiet in her orbit",
            scent="Old vellum, rose incense, and struck tuning forks",
            description=(
                "Lira seems born of cathedral shadow and song. She moves as if accompanied by an unseen chorus, "
                "her every motion framed in sacred cadence. Her silence speaks volumes — but when she sings, truths tremble."
            )
        ),
        secrets=[
            "She once harmonized with a relic linked to the Forbidden Sixth — and still carries its tonal residue.",
            "Keeps a sealed psalm-scroll written by her disgraced father — unread, but never discarded."
        ],
        motivations=[
            "Restore lost chords that may bridge the Five and the Sixth.",
            "Unravel the harmonic decay quietly spreading through the Choir’s sacred sites.",
            "Protect the innocent from doctrinal dissonance disguised as purity."
        ],
        weapons=["Echo-blade (ritual tuning dagger)", "Voice-based resonant pulse glyphs"],
        known_publicly=[
            "Leads sacred rites across Solenne’s lesser shrines.",
            "Sings in funerary harmonics known to ease the dying into peaceful dreams."
        ],
        public_knowledge=[
            "Trusted by the Exarch despite occasional divergence in interpretation.",
            "Rumored to have perfect tonal recall — even of forbidden hymns."
        ],
        private_knowledge=[
            "Harbors doubts about the Choir’s rejection of certain ancient resonances.",
            "May be able to reconstruct a chord once used to seal the Vault of Rain."
        ],
        role_in_campaign=(
            "Lira may serve as a spiritual guide, a reluctant rebel, or a tonal key to unlocking glyphic sanctums. "
            "Her music touches what even magic cannot."
        ),
        personality_traits=["Empathetic, careful, quietly defiant when truth demands"],
        narrative_hooks=[
            "Could recruit the party to retrieve a resonance stone lost in a temple collapse.",
            "Might warn of a Choir schism the Exarch refuses to acknowledge."
        ],
        plot_hooks_and_interactions=[
            "Her tonal memory may complete a glyph-sequence half-buried in time.",
            "Her father’s sealed psalm could be tied to a forbidden glyph that survived the Shattering."
        ],
        notable_quotes=[
            "Truth does not always sing in key — but it always carries.",
            "Even dissonance has its place, if you dare to listen fully."
        ]
    ),
    "thessa_varn": NPC(
        name="Thessa Varn",
        title="Kindled Flame of the Ashen Vale",
        race="Human (Touched by the Fourth Strand)",
        age="36",
        pronouns="She/Her",
        alignment="Chaotic Neutral",
        affiliation="Ashen Vale",
        aliases=["The Ember-Wrought", "Kindled Tongue", "Ashbearer"],
        background=(
            "Thessa was born in the smoldering outcrofts of Vel Sura, where ash from the ancient pyres still coats the earth. "
            "The descendant of pilgrims who once witnessed Rain D'Lacourte's firewalk, she was raised in a doctrine that viewed flame not as destruction, but refinement. "
            "Marked at thirteen by a spontaneous emberburst during meditation, Thessa was declared Kindled — a sign the flame of Rain had touched her soul. "
            "Since then, she has guided the Ashen Vale in rites of trial, passion, and renewal by fire."
        ),
        overview=(
            "Radiant and terrifying in equal measure, Thessa is the incarnation of the Ashen Creed’s belief: that only through burning can one become true. "
            "Her charisma is volcanic, her faith unwavering, and her presence demands reckoning."
        ),
        appearance=Appearance(
            alias="The Ember-Wrought",
            gender="Female",
            age="36",
            species="Human",
            height="5'10\"",
            build="Athletic, fire-dancer’s frame with coiled strength",
            eyes="Glowing ember-orange, flecked with living flame when impassioned",
            hair="Shorn short, smoldering at the roots — sometimes literally",
            skin="Bronzed with patches of soot-stained ritual markings",
            voice="Sultry contralto that cracks with heat during sermon or fury",
            clothing="Ceremonial ashen wraps over coal-stitched armor; ember-laced gauntlets",
            accessories="Braided flame beads, scorched pendant bearing Rain’s sigil, prayer-brand on shoulder",
            aesthetic="Priestess of passion, clad in sermon-fire and reverent ruin",
            aura="Hot and compelling — like standing too close to truth as it burns away lies",
            presence="Magnetic and consuming — one does not merely notice Thessa, they are *seared* into attention",
            scent="Smoldering incense, sweat, and old campfires",
            description=(
                "Thessa walks like a sermon ablaze. She speaks to the parts of the soul hidden in shame and dares them to burn clean. "
                "Her followers claim her gaze alone can set falsehood alight — and leave only truth in its wake."
            )
        ),
        secrets=[
            "Believes Rain D’Lacourte was never meant to be a Vestal — that she *hijacked* her flame by force.",
            "Is haunted by nightly visions of a burning city that does not yet exist — she calls it the Ember Future."
        ],
        motivations=[
            "Spread the Ember Creed to flame-dormant regions of Agasan.",
            "Prove that purification must precede unity — even if it scorches the world first.",
            "Ignite a second firewalk ceremony that Rain herself once forbade."
        ],
        weapons=["Emberbrand staff", "Pyre-laced shortblade", "Molten glyphs carved into her palms"],
        known_publicly=[
            "Conducts fire-purification rites attended by thousands across the Vale.",
            "Survived walking across magma unscarred — twice."
        ],
        public_knowledge=[
            "Leads the Ashen Vale’s Ember Tongue faction with both fire and mercy.",
            "Speaks of Rain not as a goddess, but as a *mirror too bright to ignore.*"
        ],
        private_knowledge=[
            "Keeps a scorched glyph fragment under her altar that flickers with forbidden hues.",
            "Has considered immolating herself before her followers… to see what might emerge from the ashes."
        ],
        role_in_campaign=(
            "Thessa can challenge the party’s convictions, test their purity, or offer them transformation through fire — literal or spiritual. "
            "She may serve as prophet, villain, or forge-mother depending on what they carry into her flames."
        ),
        personality_traits=["Fervent, fearless, speaks like prophecy"],
        narrative_hooks=[
            "May ask the party to retrieve Rain’s lost firewalk sandals from a sealed pyre-sanctum.",
            "Could task them with judging whether a captured apostate should be burned or forgiven — in front of the crowd."
        ],
        plot_hooks_and_interactions=[
            "She may hold the key to decoding a glyph that only responds to flame-kissed blood.",
            "A prophecy she utters in passing could later match a city the party visits — right before it burns."
        ],
        notable_quotes=[
            "Truth is not found in silence or shadow. It is *screamed* in fire until only its bones remain.",
            "Burn with purpose — or be kindling for someone else's lie.",
            "Rain did not give us fire to warm — but to *become.*"
        ]
    ),
    "alarith_burnedwalker": NPC(
        name="Alarith",
        title="Burned-Walker of the Ashen Vale",
        race="Tiefling",
        age="47",
        pronouns="He/Him",
        alignment="Neutral Good",
        affiliation="Ashen Vale",
        aliases=["Ash-Treader", "The Burned One", "Smokeless Pilgrim"],
        background=(
            "Alarith was once a wandering priest of a minor fire cult before witnessing the Ashen Rite — an act of self-immolation that did not kill but transfigured him. "
            "He emerged from the blaze blistered, blinded in one eye, and marked by the Vale’s mysterious flame. Since then, he has walked barefoot across the scorched places of the world, carrying embers to the forgotten and rites to the grieving. "
            "His presence is not commanding, but constant — like heat you only notice when it’s gone."
        ),
        overview=(
            "Quiet, seared by truth, and burdened with memory, Alarith bears fire not to purge but to mourn. "
            "He is the Ashen Vale’s heart of compassion beneath its fury."
        ),
        appearance=Appearance(
            alias="The Burned One",
            gender="Male",
            age="47",
            species="Tiefling",
            height="6'0\"",
            build="Lanky, limping from an old injury; wiry muscle",
            eyes="One coal-black orb, one milky-white burn-scarred socket",
            hair="None — scalp and brows seared clean",
            skin="Pale gray marbled with burn scars and soot tattoos",
            voice="Low and rasped, like smoke scraping stone",
            clothing="Tattered robes stitched from ashcloth, prayer-braids woven through the seams",
            accessories="A charred censer, belt of holy ember relics, scorched prayer beads",
            aesthetic="Pilgrim of ruin — fire-saint worn thin by grief and journey",
            aura="Somber warmth — like the last embers of a funeral pyre",
            presence="Still and reverent — others lower their voices around him without knowing why",
            scent="Old woodsmoke, dried herbs, fire-bloom oil",
            description=(
                "Alarith is the mourner of those the fire forgets. He chants for the lost, whispers blessings over bones, and scatters sacred ash where healing must begin. "
                "Even the most zealous in the Vale pause when he speaks."
            )
        ),
        secrets=[
            "Carries a sealed urn containing the ashes of the first failed Kindled — a martyr or a mistake, he will not say.",
            "His scars are glyphs — not from the fire, but from the sigils beneath it."
        ],
        motivations=[
            "Ensure the Vale’s passion does not eclipse its compassion.",
            "Guide the next generation of Kindled with care, not force.",
            "Protect Thessa Varn from the cost of her own fire."
        ],
        weapons=["Incense-wreathed staff", "Hidden flame-glyph etched along spine", "Ash-forged sickle"],
        known_publicly=[
            "Has walked across every active fireline of the Vale.",
            "Delivers ash-rites to those who cannot attend the Ember Sermons."
        ],
        public_knowledge=[
            "Rarely speaks unless it is a funeral or absolution.",
            "Once wept for a city he had never seen — three days before it burned."
        ],
        private_knowledge=[
            "Once served as Thessa Varn’s mentor — before she Kindled and outshone his teachings.",
            "Wears a ring of scorched silver — its twin belonged to a Vestal flame acolyte lost in the Shattering."
        ],
        role_in_campaign=(
            "Alarith can offer quiet wisdom, lore of forgotten fire-rites, or a path of healing through ruin. "
            "He may request the party carry his ashes should he fall — to a place even Thessa fears."
        ),
        personality_traits=["Patient, mournful, deeply principled"],
        narrative_hooks=[
            "Asks the party to deliver sacred ash to an exiled heretic of the Vale.",
            "Offers to trade a relic — but only in return for a night spent recounting who they’ve lost."
        ],
        plot_hooks_and_interactions=[
            "Knows a song that can open flame-sealed vaults — but sings it only in grief.",
            "His staff is inscribed with forgotten glyphic sigils buried by the Order."
        ],
        notable_quotes=[
            "Not all fire cleanses. Some merely reminds us we were never whole to begin with.",
            "The ash remembers what flame forgets.",
            "Do not thank me. Thank the ones who stayed burning long enough to be seen."
        ]
    ),
    "sister_crave": NPC(
        name="Sister Crave",
        title="Flame-Evangel of the Ember Tongue",
        race="Human",
        age="38",
        pronouns="She/Her",
        alignment="Chaotic Neutral",
        affiliation="Ashen Vale",
        aliases=["The Ember-Tongued", "Crave-the-Blaze", "Preacher of Ash"],
        background=(
            "Once a low-born itinerant preacher with no creed to call her own, Crave wandered the Scorched Marches muttering revelations to fire. "
            "She was taken in by the Ashen Vale after setting ablaze a heretical text — only for glyphs to dance in the smoke. "
            "Now she is the incendiary soul of the Ember Tongue, a fringe sect within the Vale that believes flame is not truth’s purifier, but its amplifier."
        ),
        overview=(
            "Unhinged, luminous, and dangerous in her passion, Sister Crave breathes gospel in sparks and scorches scripture into flesh. "
            "To some, she is a prophetess. To others, a pyromaniac too holy to silence."
        ),
        appearance=Appearance(
            alias="The Ember-Tongued",
            gender="Female",
            age="38",
            species="Human",
            height="5'6\"",
            build="Lean and wiry, as if always just post-fast",
            eyes="Molten amber with tiny flares at the edges",
            hair="Blackened at the ends, otherwise crimson-streaked and shorn unevenly",
            skin="Bronzed, burnt in places, painted with soot-glyphs",
            voice="Raspy alto like flint striking iron, crescendos with fervor",
            clothing="Ember-robe stitched from fire-resistant hymncloth and ash-veils",
            accessories="Char-blessed scrolls, chain of scorched medallions, glyph-burnt prayer stone",
            aesthetic="Street prophet fused with firebrand mystic",
            aura="Electric tension — she carries the potential to ignite belief or panic",
            presence="Magnetic — people lean closer even as they flinch",
            scent="Burnt sage, sulfur, wax tears, charred myrrh",
            description=(
                "Sister Crave is the flicker before ignition — a zealot who sings in flames. "
                "She preaches in alleys, caves, and ruins — anywhere embers may catch. Her sermons leave scars."
            )
        ),
        secrets=[
            "She once ignited a cursed reliquary — and claimed to see a vestal whisper in the flame.",
            "The soot-glyphs on her skin are unstable — one may awaken if she dies, or lies."
        ],
        motivations=[
            "Spread the gospel of the Ember Tongue beyond the Vale.",
            "Discover the lost verses said to be sung only during firestorms.",
            "Force the Temple Ascendant to admit its cowardice before holy flame."
        ],
        weapons=["Fire-chain censer", "Ash-dagger inscribed with ‘Truth Must Burn’", "Flame glyphs tattooed into her forearms"],
        known_publicly=[
            "Once held a sermon that lit an entire canyon ablaze — and emerged untouched.",
            "Speaks in fire-miracles when overcome by fervor."
        ],
        public_knowledge=[
            "Her sect is controversial even within the Ashen Vale.",
            "Believed to have burned her own tongue once — now reborn with fire’s will."
        ],
        private_knowledge=[
            "She writes her most dangerous sermons in wax — and melts them after memorizing.",
            "Carries the ashes of a past lover — one she claims was fire-born and flame-taken."
        ],
        role_in_campaign=(
            "Crave can serve as a wildcard prophet, incendiary guide, or dangerous cultic ally. "
            "She may offer the party secret truths — but at the price of burning bridges, both literal and social."
        ),
        personality_traits=["Frenzied, poetic, terrifyingly sincere"],
        narrative_hooks=[
            "Offers to burn a party member’s regret — in exchange for a vow they don’t understand.",
            "Asks the players to retrieve a fire-blessed relic from a temple buried in cooled lava."
        ],
        plot_hooks_and_interactions=[
            "Could awaken a dormant glyph in the party — whether they want it or not.",
            "May reveal a vision of the Sixth Strand, but only through a rite that risks immolation."
        ],
        notable_quotes=[
            "Flame is not cruel. It’s just louder than doubt.",
            "Let the lie burn. If something dances in the ashes, *that* was truth.",
            "I do not worship fire. I listen when it speaks."
        ]
    ),
    "samriel_thorne": NPC(
        name="Samriel Thorne",
        title="Echo-Keeper of the First Light",
        race="Half-Elf",
        age="61",
        pronouns="He/Him",
        alignment="Lawful Neutral",
        affiliation="Canticle of the First Light",
        aliases=["The Memory-Binder", "Thorne of the Pre-Sung"],
        background=(
            "Samriel was born in the cloister-hollows of the Saphirane Ducts, where chants echo in silence until they find memory. "
            "Taken as a child by the Canticle, he was shaped by resonance-lore and entrusted with the First Light — a glyphic harmony said to echo the Loom’s first pulse. "
            "Now an elder seer, Samriel catalogs reverent memory into harmonic spires, binding the forgotten to stillness. "
            "He is both keeper and curator — never the song itself, only its returning."
        ),
        overview=(
            "Measured, reverent, and woven through with ritual, Samriel sees memory as the holiest form of law. "
            "He speaks seldom and with intention — the kind of voice that folds time around itself."
        ),
        appearance=Appearance(
            alias="The Memory-Binder",
            gender="Male",
            age="61",
            species="Half-Elf",
            height="6'0\"",
            build="Slender and upright, posture shaped by ritual constraint",
            eyes="Pale silver ringed with muted gold",
            hair="Shoulder-length and ash-gray, braided with thread-beads of silence",
            skin="Ivory toned with faint blue-glyph shimmer beneath the temples",
            voice="Baritone layered with harmonics — a voice that resonates more than speaks",
            clothing="Saphirane vestments lined with harmonic glyph-weave, mirrored cuffs, and memory-braid sashes",
            accessories="Resonance stone pendulum, echo-glass spectacles, tome of sung sigils",
            aesthetic="Clerical archivist born of chant and stillness",
            aura="Subtle yet radiant — like standing beside a great bell just before it rings",
            presence="Gravely respectful — draws silence around him like a cloak",
            scent="Worn vellum, cedar ash, echo-lily",
            description=(
                "Samriel Thorne is a walking psalm, his very bearing an invocation. "
                "He does not forget — not out of defiance, but out of reverence. "
                "To walk with him is to feel the air thick with unspoken harmonies and lost prayers unburied."
            )
        ),
        secrets=[
            "He carries within his mind a living harmony — the First Light — that is slowly overwriting his identity.",
            "He once altered a sacred record to protect a child who was never meant to be remembered."
        ],
        motivations=[
            "Preserve the exact harmonic truth of history — not its facts, but its resonance.",
            "Ensure the First Light remains unsung until the Loom echoes again.",
            "Train a successor before the harmony inside him completes its rewrite."
        ],
        weapons=["Ritual dagger (never drawn)", "Voice-based harmonic glyphs", "Echo-forged bell scroll"],
        known_publicly=[
            "Has not left the Canticle sanctums in over thirty years.",
            "Known to remember conversations word-for-word — even those decades old."
        ],
        public_knowledge=[
            "Believed to be able to recall forgotten languages purely from echo-exposure.",
            "Said to have refused three glyphmasters who sought to court the Canticle."
        ],
        private_knowledge=[
            "Carries a latent glyph inside his mind that may unravel into sound when he dies.",
            "Once whispered a truth that made a saint weep and renounce her title."
        ],
        role_in_campaign=(
            "Samriel may serve as an ancient witness, a key to unlocking forgotten lore, or an anchor when memory frays. "
            "He will not act, but will remember *why* the party must."
        ),
        personality_traits=["Grave, serene, slow to speak, never forgets a word"],
        narrative_hooks=[
            "May request the party retrieve a lost harmonic fragment from a ruin where time bends.",
            "Could guide them into a ritual where their memories must be harmonized — or sacrificed."
        ],
        plot_hooks_and_interactions=[
            "May hold a memory the players do not recall — but which changes everything.",
            "His resonance could awaken glyphic echoes in places thought long silent."
        ],
        notable_quotes=[
            "The song you forgot? It remembers *you.*",
            "Memory is not for keeping. It is for *keeping true.*",
            "I have no opinion. Only echo."
        ]
    ),
    "ashadel_ninth_orbit": NPC(
        name="Asha'del",
        title="Loomwatch of the Ninth Orbit",
        race="Eladrin",
        age="Unknown (appears mid-30s)",
        pronouns="She/They",
        alignment="Neutral Good",
        affiliation="Canticle of the First Light",
        aliases=["Star-Sister", "The Celestial Scribe", "Orbit-Bound"],
        background=(
            "Asha'del was once a dusk-born wanderer of the Feywild’s edge, until a whisper from the stars led her to Alorin. "
            "Drawn by harmonic anomalies and glyphs resonating in planetary orbits, she joined the Canticle not as devotee, but as navigator. "
            "She now charts the Loom's outer pulses, decoding astral echoes and chasing the ninth resonance — a theoretical pattern she believes connects the gods, glyphs, and gravity itself."
        ),
        overview=(
            "Asha'del is curious, dreamlike, and dazzlingly brilliant — a scholar whose truths arrive as starlight does: slow, pure, and precise. "
            "Her presence is unsettling only because it feels like she already knows what you will become."
        ),
        appearance=Appearance(
            alias="Star-Sister",
            gender="Fluid (Feminine-aligned)",
            age="Appears mid-30s",
            species="Eladrin",
            height="5'11\"",
            build="Graceful, willow-thin, weightless in step",
            eyes="Iridescent, star-pupiled — shimmer with violet or sapphire depending on focus",
            hair="Midnight black threaded with constellations that slowly shift",
            skin="Luminous pale with a faint dusting of stardust freckles",
            voice="Soft alto, with the cadence of distant chimes or moonlit water",
            clothing="Canticle robes spun with orbit-thread and astral script, layered with maps of moving light",
            accessories="Gyroscope pendant, astral lens monocle, constellation scrolls",
            aesthetic="Astronomer-priestess with a dreamer’s soul",
            aura="Otherworldly serenity, as if standing beneath a vast and silent sky",
            presence="Contemplative and slow-moving, as if gravity does not pull her the same way",
            scent="Night jasmine, celestial ink, ozone after a comet's pass",
            description=(
                "Asha'del is more than mortal scholar — she is a hymn sung between stars. "
                "Though grounded in the Canticle’s sanctum, her mind orbits the truths beyond it. "
                "Her words form orbits around deeper ideas, drawing others into the gravity of her knowing."
            )
        ),
        secrets=[
            "Knows the Canticle has charted nine orbits, but only eight are acknowledged. She believes she is part of the ninth.",
            "Her true name is written in a glyph only visible during full eclipses — and she does not speak it aloud."
        ],
        motivations=[
            "Map the final orbit that binds divine will to the Loom's first glyph.",
            "Teach others to read resonance the way stars speak: in long, looping harmonies.",
            "Reveal that the Loom was not woven — it is still weaving."
        ],
        weapons=["Glyph-etched star-daggers", "Astral projection via orbit focus", "Sigil-mirror of celestial defense"],
        known_publicly=[
            "Charts constellations that match ancient glyphic patterns across ruins.",
            "Believed to have once disappeared for an entire year and returned unchanged — or perhaps changed entirely."
        ],
        public_knowledge=[
            "One of the most reclusive scholars of the Canticle.",
            "Willing to teach if asked respectfully — but requires ritual preparation first."
        ],
        private_knowledge=[
            "Has seen the ninth strand — but only as a dream overlapping reality.",
            "Knows the exact moment when the stars will no longer speak to Alorin."
        ],
        role_in_campaign=(
            "Asha’del can guide players to celestial glyphs, serve as a divinatory source for cosmic phenomena, or provoke deeper existential arcs. "
            "Her aid will come slowly, but with gravity and consequence."
        ),
        personality_traits=["Measured, introspective, celestial-minded", "Patient beyond comprehension"],
        narrative_hooks=[
            "Might offer a reading of a star-forged glyph — but only under the correct sky.",
            "Could request help retrieving an orbit shard that fell to earth in a forbidden crater."
        ],
        plot_hooks_and_interactions=[
            "May be the only one who understands how the Loom reacts to stellar shifts.",
            "Her glyphs might reveal the location of a forgotten Vestal... or the moment one will rise again."
        ],
        notable_quotes=[
            "The stars don’t answer. They echo.",
            "You were written before you were born — I simply help you read the line you are.",
            "Orbit is not motion. It’s *memory,* circling gravity’s truth."
        ]
    ),
    "nunav_varn": NPC(
        name="Nunav Varn",
        title="Threadbearer of the Canticle",
        race="Human (Glyph-Touched)",
        age="62",
        pronouns="He/Him",
        alignment="Lawful Neutral",
        affiliation="Canticle of the First Light",
        aliases=["Last of the Unravelers", "The Silent Thread", "Unbroken Varn"],
        background=(
            "Nunav Varn is a direct descendant of one of the twenty glyph-bound nobles who received power in the wake of Bjorn's death — though his line rejected the Keepers' legacy. "
            "Unlike his siblings who pursued power, Nunav withdrew into glyphic study and contemplation, choosing silence over legacy. "
            "He was named Threadbearer by the Canticle’s former stewards, tasked with guarding the knowledge that should *never* be woven again."
        ),
        overview=(
            "Nunav is quiet, devout, and weary — a custodian of forbidden strands whose very presence carries the weight of memory. "
            "He speaks rarely, and never to fill silence. His words are threads pulled only when absolutely necessary."
        ),
        appearance=Appearance(
            alias="The Silent Thread",
            gender="Male",
            age="62",
            species="Human (Glyph-Touched)",
            height="6'0\"",
            build="Tall and gaunt, with limbs like parchment spindles",
            eyes="One black, one silver-threaded white",
            hair="Thin and chalk-white, drawn into a low knot at the nape",
            skin="Ashen with ink-seeped veins along the temples",
            voice="Dusty baritone, like a prayer whispered over old vellum",
            clothing="Canticle vestments over moth-gray robes, glyph-script woven down the hem",
            accessories="Inkstone rosary, vow-threaded bracer, satchel of uninked scrolls",
            aesthetic="Scribe-priest, scholar of the unspeakable",
            aura="A stillness that absorbs movement — like entering a memory too sacred to touch",
            presence="Gravely serene — people lower their voices around him without realizing it",
            scent="Old parchment, candle ash, seal-wax",
            description=(
                "Nunav carries knowledge not as a weapon, but as a wound. "
                "He walks the halls of the Canticle tracing half-erased glyphs in the air, lips moving in memory’s silence. "
                "When he speaks, even echoes seem to listen."
            )
        ),
        secrets=[
            "He carries within his blood the dormant sixth glyph — not active, but present, a living vault.",
            "Once tried to erase himself from the Canticle’s records, believing his presence was too dangerous to remain."
        ],
        motivations=[
            "Prevent the forbidden glyphs from being rewritten into the world.",
            "Train a successor who will remember without temptation.",
            "Uncover the purpose of the Ninth Orbit — not to use it, but to ensure it is never abused."
        ],
        weapons=None,
        known_publicly=[
            "Is never seen outside the Canticle’s innermost sanctum.",
            "Only speaks during rites of remembrance — and even then, only in glyph-verse."
        ],
        public_knowledge=[
            "His lineage ties him to the Keepers, though he does not acknowledge it.",
            "Regarded as the most trusted steward of pre-Shattering glyphic memory."
        ],
        private_knowledge=[
            "May be the only one who knows where the original glyph of Bjorn’s death was sealed.",
            "Has encoded a memory within a living strand — a verbal glyph that, once spoken, cannot be forgotten."
        ],
        role_in_campaign=(
            "Nunav can serve as gatekeeper, moral weight, or final witness to a truth the players were never meant to unearth. "
            "He may grant access to ancient knowledge, or deny it at great cost."
        ),
        personality_traits=["Grave, deeply patient, haunted by inheritance"],
        narrative_hooks=[
            "Might ask the party to return a lost page from the Varn ledger — one that names those who broke the First Light.",
            "Could task the players with finding his successor, who unknowingly carries a glyph-fragment in their dreams."
        ],
        plot_hooks_and_interactions=[
            "Unlocking his secrets could shift the entire campaign's relationship to glyphs.",
            "May sacrifice himself to prevent a glyph from being spoken aloud."
        ],
        notable_quotes=[
            "Some threads do not bind. They *warn.*",
            "We are not meant to *use* the Loom — only to keep it from unraveling.",
            "My name is Varn. I carry what my house broke, and I will not let it break again."
        ]
    ),
}