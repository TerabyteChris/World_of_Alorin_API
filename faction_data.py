from models import Faction

raw_factions = {
    "sigil_covenant": Faction(
        name="The Sigil Covenant",
        ideology="Glyphs cannot be undone — only controlled...",
        alignment="Lawful Neutral",
        origin="A faction of surviving Keepers...",
        structure="Cell-based network...",
        known_leaders=["Archivist Varn Telion", "Cloaked Concord"],
        seat_of_power="The Vault of Quiet",
        symbols=["A cracked glyph sealed by six threads", "The binding ring"],
        methods=["Counterglyph design", "Null-script rituals"],
        influence="Widespread but subtle...",
        public_perception="Respectful but fearful...",
        secrets_known=["Maintain a ledger of all known living glyph-bearers..."],
        player_interactions=[
            "Can offer assistance in suppressing unstable glyphs...",
            "Might conscript the party..."
        ],
        rivals=["The Order", "Temple Ascendant"],
        allies=["Select clergy", "sympathetic nobles"],
        notable_quotes=[
            "Power unbound is death prolonged.",
            "We are not censors. We are stitches across a wound that will not close."
        ]
    ),
    "silent_archive": Faction(
        name="The Silent Archive",
        ideology="Preservation without influence. Knowledge must endure untouched by power.",
        alignment="True Neutral",
        origin="One of the three Keeper splinters after the murder of Bjorn. The Archive rejected both suppression and empowerment, choosing instead to vanish.",
        structure="Decentralized cells sealed in ancient towers, crypt-libraries, and glyph-buried mountain halls.",
        known_leaders=["The Quietest Pen (rumored)"],
        seat_of_power="Unknown — only glimpses of towers in the far east or north are whispered.",
        symbols=["An inkless quill over a closed eye", "Three concentric silence rings", "Script runes bound in barbed loops"],
        methods=["Memory warding", "paradox glyph locks", "time-fractured record scrolls", "mnemonic containment rites."],
        influence="Minimal direct influence. Their tomes are sought by scholars, cults, and madmen — but their locations remain almost entirely lost.",
        public_perception="Myth. Some believe the Archive never existed, only a metaphor for knowledge lost to time.",
        secrets_known=[
            "Hold original glyph-scripts of the Five Strands, as well as fragments of the Forbidden Sixth.",
            "Possibly retain one of the last uncorrupted memories of Bjorn Van Gelderan."
        ],
        player_interactions=[
            "A glyph the players find may contain an Archive watermark — and begin whispering directions toward one of their towers.",
            "An Archive agent may seek the party to rescue a stolen sigil-script lost in the world."
        ],
        rivals=["The Order", "The Temple Ascendant"],
        allies=["The Sigil Covenant (loosely, distrustfully)"],
        notable_quotes=[
            "Ink holds. Voice sways. We do not speak — we *remember.*",
            "The Archive endures because it does not act."
        ]
    ),
    "the_order": Faction(
        name="The Order",
        ideology="Glyphs are our birthright. The sacrifice of Bjorn was not blasphemy — it was genesis.",
        alignment="Neutral Evil",
        origin="Originally the inner circle of the Keepers, who engineered the murder of Bjorn. Cast out, they evolved over centuries into a glyphic cabal known only through rumor.",
        structure="Cellular, decentralized, with sleeper agents embedded across noble courts, research labs, and ruin cults.",
        known_leaders=["Unknown. Only the title 'The Rewoven' is ever spoken aloud."],
        seat_of_power="None confirmed. Some believe they operate from a shifting hidden fortress called 'The Lattice.'",
        symbols=["A stylized eye woven into a glyphic helix", "Six hands reaching toward a broken loom", "The Spiral Sigil — seen only in hallucinations"],
        methods=["Genetic glyph inheritance, forced Awakening, illegal relic crafting, myth rewriting, sacrificial rites."],
        influence="Hidden, but vast. Strange coincidences and sudden glyph outbreaks often trace back to their manipulation.",
        public_perception="Denied. Most authorities don’t believe The Order exists — or claim to know nothing of it.",
        secrets_known=[
            "May have crafted the first synthetic glyphborne Noble.",
            "Possess fragments of the Forbidden Sixth that the Archive believes lost."
        ],
        player_interactions=[
            "An ally may be revealed as a glyph-host — and an unwilling vessel for the Order’s next Noble.",
            "The party may uncover a laboratory disguised as a monastery experimenting on orphans with 'unusual' dreams."
        ],
        rivals=["Sigil Covenant", "Silent Archive", "Null Orders"],
        allies=["Whispering Chain (transactional)", "Pale Choir (theologically aligned but unstable)"],
        notable_quotes=[
            "We did not break the world — we opened its eyes.",
            "From blood and loom, we make the new divine."
        ]
    ),
    "gilded_fold": Faction(
        name="The Gilded Fold",
        ideology="Wealth sanctifies. Coin is covenant. The divine chooses the prosperous — and we are their instruments.",
        alignment="Lawful Evil",
        origin="Formed in the power vacuum after the Shattering, the Fold emerged from a cabal of merchant priests and contract seers who fused finance with faith.",
        structure="Merchant-theocracy. Governed by the Concordium: twelve masked arbiters representing the major trade temples.",
        known_leaders=["Chancellor-Mask of Ledros", "Vicar Maru of the Fifth Ledger"],
        seat_of_power="The Golden Vault-Cathedral of Vael Alura — a holy bank, temple, and auction house.",
        symbols=["A closed palm with golden ink flowing upward", "Scales over a burning contract", "The Coin-Wheel of Ascension"],
        methods=[
            "Binding oaths through blood-gold sigils",
            "Economic coercion via glyph-warded trade routes",
            "Sanctification of mercantile success as divine favor"
        ],
        influence="Vast, though rarely obvious. They control minting rights in many cities and fund reconstruction in exchange for spiritual and political debt.",
        public_perception="Varies — revered in the east as bringers of prosperity, reviled in the north as holy usurers.",
        secrets_known=[
            "Funded multiple heretical expeditions seeking to forge new glyphs through alchemical means.",
            "Possess a copy of the original ledger from the Van Gelderan sacrifice — hidden beneath their cathedral vault."
        ],
        player_interactions=[
            "Party may be offered funding for their quest — but the terms bind more than coin.",
            "A town's clergy may have been replaced by Fold auditors preaching spiritual debt forgiveness for a price."
        ],
        rivals=["The Silent Archive", "Outer Chorus", "Pale Choir"],
        allies=["Temple Ascendant", "Some lesser noble houses"],
        notable_quotes=[
            "Blessed is the contract unbroken. Holy is the debt that uplifts.",
            "Even the divine signs receipts."
        ]
    ),
    "whispering_chain": Faction(
        name="The Whispering Chain",
        ideology="The strongest glyphs are not learned — they are inherited. Blood remembers what parchment forgets.",
        alignment="Chaotic Neutral",
        origin="Rumored to have emerged from the mad remnants of Keeper bloodlines. They believe certain lineages carry dormant glyphs—waiting to awaken through trauma, ritual, or convergence.",
        structure="Matrilineal covens and bastard houses, each bound by ancestral sigil-brands. No central leadership — only the 'Voice in Crimson', a dream-tethered seer said to speak for the Chain as a whole.",
        known_leaders=["High-Mother Sevet of the Pale Vow", "The Voice in Crimson (location unknown)"],
        seat_of_power="None permanent. Covens drift between haunted estates, ruin-fortresses, and dead birthing halls.",
        symbols=["A shackle made of bleeding script", "A chain curled into a womb", "The twin masks of lineage: one blank, one branded"],
        methods=[
            "Glyph infusion via bloodline intermarriage",
            "Trauma-based glyph ignition",
            "Blood-singing rites that call to dormant ancestors"
        ],
        influence="Liminal but spreading. Operate on the fringes of society — particularly among orphans, abandoned noble lines, and 'wasteling' camps.",
        public_perception="Feared and misunderstood. Often conflated with witches, blight-mothers, or plague midwives.",
        secrets_known=[
            "Have successfully bred a line of twins who each hold half of a Forbidden glyph — and only function when near one another.",
            "Are attempting to locate and recover Bjorn Van Gelderan's true descendant."
        ],
        player_interactions=[
            "Party discovers a glyph awakening in a child — only to find the Chain already watching.",
            "An NPC ally may secretly belong to the Chain and become unstable under stress, awakening blood-borne sigils."
        ],
        rivals=["Sigil Covenant", "Temple Ascendant", "Gilded Fold"],
        allies=["The Order (occasional breeding alliances)", "The Pale Choir (through shared blood rites)"],
        notable_quotes=[
            "The past lives in marrow. We are only the vessel.",
            "The Chain does not bind — it remembers."
        ]
    ),
    "outer_chorus": Faction(
        name="The Outer Chorus",
        ideology="Truth cannot be imprisoned. Glyphs are echoes of the first song — and song belongs to the people.",
        alignment="Chaotic Good",
        origin="Formed from splintered bards, failed clerics, disillusioned glyphbearers, and dreamers exiled by both temple and throne. The Chorus believes glyphs are a divine chorus meant to be shared — not controlled.",
        structure="No central hierarchy. Operates as a network of masked 'echo cells' who share forbidden chants, counter-glyphs, and mnemonic rituals through oral performance and illusion.",
        known_leaders=["Chorus-Mask Kiva Thren", "The Ragman of Vel Trast", "The One-Who-Whistles"],
        seat_of_power="None fixed — but whispers speak of the 'Crescendo Below', a moving amphitheater stitched from buried catacombs and old performance halls.",
        symbols=["A cracked mask dripping ink", "A mouthless face with open ears", "The spiral tongue"],
        methods=[
            "Glyph evocation through melodic resonance",
            "Disruption of ritual wards via harmonic collapse",
            "Public performance as protest, confession, and invocation"
        ],
        influence="Surprisingly vast among common folk, traveling troupes, and excommunicated clergy. Their verses spread faster than flames.",
        public_perception="A paradox: seen as dangerous heretics by rulers, beloved saviors by the downtrodden.",
        secrets_known=[
            "Their founder was once a Vestal-in-training who escaped glyph-purging at the last moment.",
            "Some members bear partial echoes of the Forbidden Sixth — unknowingly shaping it anew through sound alone."
        ],
        player_interactions=[
            "Party might be drawn into a performance that rewrites their memory — or restores a forgotten truth.",
            "A wanted Chorus bard seeks asylum and offers the players a chant that opens sealed glyphic wards."
        ],
        rivals=["Temple Ascendant", "Sigil Covenant", "Gilded Fold"],
        allies=["The Silent Archive (secret correspondence)", "Some branches of The Order"],
        notable_quotes=[
            "Even a whisper can unmake a wall.",
            "We do not wield glyphs — we remember how they danced."
        ]
    ),
    "stormbound_synod": Faction(
        name="The Stormbound Synod",
        ideology="The storm speaks with glyphs older than the Archive. We do not read them — we listen.",
        alignment="True Neutral",
        origin="A loosely allied confederation of skyward tribes and wind-priests who believe storms are divine expressions of lost glyphic consciousness. Their traditions predate the Keepers — and they claim to remember when the sky was sentient.",
        structure="Nomadic sky-sects and summit enclaves. Leadership determined by 'Cloudmarks' — birthmarks that mimic thunder-glyphs seen during storms. The Synod gathers only during convergence-storms, where decisions are made communally.",
        known_leaders=["Torm Durei, the Rainwalker", "Mist-Caller Yev of the Hollow Peaks"],
        seat_of_power="The Skyrift Vortex — a sacred, lightning-wracked caldera where no metal may be carried and all speech must be sung.",
        symbols=["A spiral of cloud-thread around an empty eye", "Stone staffs carved with pressure glyphs", "Rain-masks made of stormbeast hide"],
        methods=[
            "Divining glyphic prophecy from thunder and wind patterns",
            "Chanting storm-liturgy to guide weather and fate",
            "Tattooing flesh with stormglyphs during rites of passage"
        ],
        influence="Regionally potent — particularly in the mountain ranges east of the Aemil Reach and the storm-swept plateaus of southern Agasan.",
        public_perception="Regarded as mad prophets, revered shamans, or dangerous weather-witches depending on the region.",
        secrets_known=[
            "A living glyph sleeps in the heart of the Skyrift — visible only when the storm sings.",
            "They possess fragments of an oral glyph language no known Archive contains — and it evolves with every generation."
        ],
        player_interactions=[
            "The party may be caught in a storm guided by the Synod to divert a disaster — or deliver an omen.",
            "A Synod elder offers storm-guidance, but requires the party surrender metal and memory alike to cross their lands."
        ],
        rivals=["Temple Ascendant", "Gilded Fold", "Sigil Covenant (ideological clashes)"],
        allies=["Outer Chorus", "Some distant Archive towers (through dream-trades)"],
        notable_quotes=[
            "Every thunderclap is a sentence. Most are warnings.",
            "The wind knows your true name. It is screaming it now."
        ]
    ),
    "pale_choir": Faction(
        name="The Pale Choir",
        ideology="The Shattering was not a tragedy. It was sacred. The death of Bjorn was the first and greatest hymn.",
        alignment="Lawful Evil",
        origin="Formed by fringe clergy and heretic nobles who believed Bjorn’s murder was not sacrilege, but divine choreography. To them, the Shattering was a ritual — not a rebellion.",
        structure="Hierophantic caste — Initiates, Cantors, and White-Veiled Exarchs. Choirs function as traveling reliquary troupes, each preserving an 'echo' of Bjorn’s final scream.",
        known_leaders=["White Exarch Rhaziel Vaen", "Cantor Lira Vannos"],
        seat_of_power="The Mausoleum of Resonant Mercy — a catacomb-turned-cathedral built around a bleeding echo-shard believed to contain Bjorn’s dying breath.",
        symbols=["A weeping mask pierced by nine needles", "An open throat with no tongue", "Ashen robes stitched with silent script"],
        methods=[
            "Choral evocations designed to fracture glyph stability",
            "Public reenactments of the Shattering as liturgical performance",
            "Soul-sundering hymns believed to 'purify' glyphbearers"
        ],
        influence="Growing in the southern borderlands and among grief-stricken temple cities where loss outweighs reason. Their doctrine spreads fastest after mass tragedies.",
        public_perception="Reviled by orthodox faiths. Considered cultists or corpse-singers by many. Yet their songs stir something undeniable.",
        secrets_known=[
            "They possess a splinter of Bjorn’s original glyph — locked in a voicebox that cannot be opened by mortal means.",
            "Some Choir members spontaneously develop unstable, trauma-bound glyphs when chanting together — suggesting a forbidden strand."
        ],
        player_interactions=[
            "A Choir procession blocks a city gate, singing the party’s sins into light.",
            "A fallen ally may be recovered — but only if the players allow their soul to be split and shared in a ‘Resonant Communion’."
        ],
        rivals=["Temple Ascendant", "Sigil Covenant", "The Order"],
        allies=["Whispering Chain (in blood rites)", "Certain fringe members of the Outer Chorus"],
        notable_quotes=[
            "He did not die in vain. He died in tune.",
            "Your grief is a hymn. Let it be sung."
        ]
    ),
    "ashen_veil": Faction(
        name="The Ashen Veil",
        ideology="Clarity is a lie. Truth must be scorched clean. Rain D’Lacourte is not salvation — she is the trial through which salvation may be glimpsed.",
        alignment="Chaotic Neutral",
        origin="Formed in the wake of Rain’s brief appearances across Agasan. Wherever she wandered, visions followed — and from those visions, seekers gathered. Not followers… witnesses.",
        structure="Decentralized fire-cults, each interpreting Rain’s words differently. The 'Kindled' lead rites. The 'Singed' serve as scribes. The 'Burned' are those who touched truth too deeply — and live mad but prophetic.",
        known_leaders=["Kindled Thessa Varn", "Burned-Walker Alarith", "Sister Crave (of the Ember Tongue)"],
        seat_of_power="None fixed. However, 'The Emberfold' — a traveling pilgrimage city built around a forever-burning brazier — is said to drift the hills east of the Vale of Teeth.",
        symbols=["A veil of smoke over open eyes", "A tongue engulfed in flame", "Spiral brands seared into the skin"],
        methods=[
            "Trial by fire — literal and metaphysical — as a form of truth purification",
            "Reenactment of Rain’s known sayings as paradox riddles and flame dances",
            "Whisper-ashes: burnt glyphic fragments inhaled during prophetic trances"
        ],
        influence="Expanding rapidly among glyph-obsessed youth, broken scholars, and exile mystics. Their rites have appeared in seven cities and thirteen burnings in the past year alone.",
        public_perception="Divisive — seen as deranged pyromancers by some, as inspired mystics by others. Official temples deny Rain’s connection to them entirely.",
        secrets_known=[
            "One branch of the Veil seeks to *become* Rain — through ritual convergence of memory, echo, and fire.",
            "They possess a seared relic from the Shattering — believed to hold Rain’s laughter, trapped in ash."
        ],
        player_interactions=[
            "A town is about to be 'cleansed' by the Veil — unless the players interpret a riddle Rain once whispered there.",
            "An NPC joins the party — a Veil pilgrim who believes one of the PCs is Rain reborn."
        ],
        rivals=["Temple Ascendant", "Sigil Covenant", "Silent Archive"],
        allies=["Outer Chorus (on chaotic terms)", "The Whispering Chain (shared reverence for paradox glyphs)"],
        notable_quotes=[
            "She never asked to be worshipped. She asked to be witnessed — and we *burned*.",
            "You seek wisdom? Then bring tinder. Rain does not wait for those who fear the flame."
        ]
    ),
    "canticle_of_the_first_light": Faction(
        name="The Canticle of the First Light",
        ideology="Creation was never meant to be ruled — only remembered. The Loom breathes still, and the Song has not ended.",
        alignment="Lawful Neutral",
        origin="No one knows exactly when the Canticle formed — only that it appears when the world forgets its first truths. They claim to serve neither glyph nor god, but the Will of the Weave — the first breath of Cephrael and the eternal spark of Epiphany.",
        structure="A triune chorus — the Echo (memory), the Threadbearers (lineage), and the Loomwatch (prophecy). Each faction acts in harmony, rotating leadership with the celestial rhythm of the old constellations.",
        known_leaders=["Echo-Keeper Samriel Thorne", "Loomwatch Asha'del of the Ninth Orbit", "Threadbearer Nunav Varn"],
        seat_of_power="The Starfold Sanctum — a hidden observatory-temple carved into the bones of a fallen Vestal, suspended above the Hollow Sky Crater.",
        symbols=["Two interlocked spirals — one perfect, one frayed", "An eye whose iris is a spinning thread", "A chord chart of ten notes, five blurred"],
        methods=[
            "Chanting the names of the lost Vestals to prevent their erasure",
            "Interpreting ripple patterns in the Loom via star glyphs",
            "Scribing 'unsung glyphs' that cannot exist unless believed in"
        ],
        influence="Subtle but ancient. The Canticle has shaped hidden turning points throughout history. They are said to appear in cities on the brink, offering impossible choices.",
        public_perception="Whispered of in high academia and deep Archive corridors. Some say they were the first Keepers. Others claim they are the Weave’s correction made flesh.",
        secrets_known=[
            "They believe Orieth the Pale is still alive — looped within the Loom, waiting to be unraveled by a mortal chord.",
            "They possess fragments of pre-Vestal memory stored in harmonic prisms — if played, they might summon echoes of the First Light itself."
        ],
        player_interactions=[
            "A member offers to rewrite a player’s past — at the cost of anchoring them to an unrevealed Strand.",
            "The Canticle requests the party retrieve a starfallen relic that burns with a Strand not yet known to history."
        ],
        rivals=["Temple Ascendant", "The Order", "Pale Choir"],
        allies=["The Silent Archive", "Stormbound Synod (celestial branch)", "Some Awakened among the Sigil Covenant"],
        notable_quotes=[
            "The stars are not above you. They are what you forgot.",
            "You are not broken. You are an unfinished verse.",
            "Cephrael weaves. Epiphany burns. You are both — if you dare."
        ]
    )

}