SIGNS = [
    "Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo",
    "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"
]

SIGN_SYMBOLS = {
    "Aries": "♈", "Taurus": "♉", "Gemini": "♊", "Cancer": "♋",
    "Leo": "♌", "Virgo": "♍", "Libra": "♎", "Scorpio": "♏",
    "Sagittarius": "♐", "Capricorn": "♑", "Aquarius": "♒", "Pisces": "♓",
}

PLANET_SYMBOLS = {
    "Sun": "☉", "Moon": "☽", "Mercury": "☿", "Venus": "♀",
    "Mars": "♂", "Jupiter": "♃", "Saturn": "♄", "Uranus": "⛢",
    "Neptune": "♆", "Rahu": "☊", "Ketu": "☋",
    "Ascendant": "↑", "Midheaven": "MC",
}

PLANET_MEANINGS = {
    "Sun":       "Core identity & life purpose",
    "Moon":      "Emotions, instincts & inner world",
    "Mercury":   "Mind, communication & perception",
    "Venus":     "Love, beauty & values",
    "Mars":      "Drive, desire & assertion",
    "Jupiter":   "Expansion, wisdom & abundance",
    "Saturn":    "Discipline, karma & life lessons",
    "Uranus":    "Innovation, freedom & awakening",
    "Neptune":   "Dreams, spirituality & dissolution",
    "Rahu":      "Desire, ambition & worldly dharma",
    "Ketu":      "Liberation, past karma & spiritual insight",
    "Ascendant": "Outward persona & life approach",
    "Midheaven": "Career, vocation & public legacy",
}

HOUSE_MEANINGS = {
    1:  "Self, identity & physical appearance",
    2:  "Money, possessions & personal values",
    3:  "Communication, siblings & local travel",
    4:  "Home, family, roots & inner foundation",
    5:  "Creativity, romance, children & pleasure",
    6:  "Health, daily work, service & routines",
    7:  "Partnerships, marriage & open enemies",
    8:  "Transformation, shared resources & death",
    9:  "Philosophy, travel, higher education & beliefs",
    10: "Career, reputation, public life & authority",
    11: "Friends, groups, hopes & collective ideals",
    12: "Hidden self, spirituality, isolation & karma",
}

# ── Nakshatra Data ───────────────────────────────────────────────────────────

NAKSHATRAS = [
    {"name": "Ashwini",            "lord": "Ketu",    "symbol": "Horse's head",      "deity": "Ashwini Kumaras"},
    {"name": "Bharani",            "lord": "Venus",   "symbol": "Yoni",               "deity": "Yama"},
    {"name": "Krittika",           "lord": "Sun",     "symbol": "Razor / Flame",      "deity": "Agni"},
    {"name": "Rohini",             "lord": "Moon",    "symbol": "Chariot",            "deity": "Brahma"},
    {"name": "Mrigashira",         "lord": "Mars",    "symbol": "Deer's head",        "deity": "Soma"},
    {"name": "Ardra",              "lord": "Rahu",    "symbol": "Teardrop",           "deity": "Rudra"},
    {"name": "Punarvasu",          "lord": "Jupiter", "symbol": "Quiver of arrows",   "deity": "Aditi"},
    {"name": "Pushya",             "lord": "Saturn",  "symbol": "Lotus / Udder",      "deity": "Brihaspati"},
    {"name": "Ashlesha",           "lord": "Mercury", "symbol": "Serpent",            "deity": "Nagas"},
    {"name": "Magha",              "lord": "Ketu",    "symbol": "Royal throne",       "deity": "Pitras"},
    {"name": "Purva Phalguni",     "lord": "Venus",   "symbol": "Hammock / Fig tree", "deity": "Bhaga"},
    {"name": "Uttara Phalguni",    "lord": "Sun",     "symbol": "Bed",                "deity": "Aryaman"},
    {"name": "Hasta",              "lord": "Moon",    "symbol": "Open hand",          "deity": "Savitar"},
    {"name": "Chitra",             "lord": "Mars",    "symbol": "Bright jewel",       "deity": "Vishwakarma"},
    {"name": "Swati",              "lord": "Rahu",    "symbol": "Young sprout / Coral","deity": "Vayu"},
    {"name": "Vishakha",           "lord": "Jupiter", "symbol": "Triumphal arch",     "deity": "Indra-Agni"},
    {"name": "Anuradha",           "lord": "Saturn",  "symbol": "Lotus",              "deity": "Mitra"},
    {"name": "Jyeshtha",           "lord": "Mercury", "symbol": "Circular amulet",    "deity": "Indra"},
    {"name": "Mula",               "lord": "Ketu",    "symbol": "Tied roots",         "deity": "Nirrti"},
    {"name": "Purva Ashadha",      "lord": "Venus",   "symbol": "Elephant tusk / Fan","deity": "Apas"},
    {"name": "Uttara Ashadha",     "lord": "Sun",     "symbol": "Tusk / Planks",      "deity": "Vishvadevas"},
    {"name": "Shravana",           "lord": "Moon",    "symbol": "Ear / Three footprints","deity": "Vishnu"},
    {"name": "Dhanishtha",         "lord": "Mars",    "symbol": "Drum",               "deity": "Eight Vasus"},
    {"name": "Shatabhisha",        "lord": "Rahu",    "symbol": "Empty circle",       "deity": "Varuna"},
    {"name": "Purva Bhadrapada",   "lord": "Jupiter", "symbol": "Sword",              "deity": "Aja Ekapada"},
    {"name": "Uttara Bhadrapada",  "lord": "Saturn",  "symbol": "Snake in water",     "deity": "Ahir Budhnya"},
    {"name": "Revati",             "lord": "Mercury", "symbol": "Fish / Drum",        "deity": "Pushan"},
]

NAKSHATRA_INTERPRETATIONS = {
    "Ashwini":           "Quick, healing, and pioneering. Ashwini carries the energy of divine healers who ride the dawn — fast beginnings, restless vitality, and an instinct to help before being asked. The soul here moves swiftly and hates delay.",
    "Bharani":           "Fertile, intense, and transformative. Bharani holds the energy of Yama — the gateway between creation and dissolution. Those with planets here carry enormous creative and destructive potential, and must learn to wield power with moral clarity.",
    "Krittika":          "Purifying, sharp, and radiant. Krittika's symbol is the flame that cuts through illusion. There is a fierce clarity and critical intelligence here, along with the capacity to nurture through high standards rather than soft accommodation.",
    "Rohini":            "Sensuous, creative, and magnetic. Ruled by the Moon and beloved of all the nakshatras, Rohini overflows with beauty, growth, and the pull of earthly abundance. Those with planets here attract what they desire with unusual ease.",
    "Mrigashira":        "Seeking, curious, and gently restless. The deer's head always searches — for beauty, for safety, for the next horizon. There is a poetic sensitivity and a nervous refinement here; the soul is always scanning for something more.",
    "Ardra":             "Raw, stormy, and transformative. Ardra is Rudra's teardrop — grief that becomes power. There is a sharp intelligence here that cuts through comfort and convention. The nakshatra of storms, breakthroughs, and radically renewed minds.",
    "Punarvasu":         "Returning, renewing, and abundant. Punarvasu means 'the return of light' — it carries the energy of the quiver that refills itself. Those with planets here have remarkable resilience and the ability to rebuild what was lost.",
    "Pushya":            "Nourishing, stable, and abundant. Pushya is considered the most auspicious of nakshatras — the lotus that blooms in still water. It carries the energy of the spiritual teacher, the devoted parent, and the faithful friend.",
    "Ashlesha":          "Penetrating, coiling, and psychologically intense. The serpent of Ashlesha sees through appearances with unnerving clarity. There is kundalini power here — the capacity for deep healing or, when misdirected, manipulation.",
    "Magha":             "Royal, ancestral, and commanding. Magha carries the energy of kings and lineages. Those with planets here are connected to ancestral power and often feel a strong pull toward legacy, pride, and authority that must be exercised with humility.",
    "Purva Phalguni":    "Creative, pleasure-loving, and radiant. The hammock of Purva Phalguni invites rest, creativity, and the full enjoyment of life's gifts. There is artistic talent, sensuality, and a magnetic charm that draws people and resources.",
    "Uttara Phalguni":   "Generous, sustaining, and loyal. Where Purva Phalguni enjoys the harvest, Uttara Phalguni shares it. This nakshatra carries the energy of the patron, the partner, and the one who builds something that endures for others.",
    "Hasta":             "Skilled, precise, and clever-handed. Hasta is the open hand of Savitar — the ability to create, heal, and manifest through skill and dexterity. There is a practical intelligence and craftsmanship here that turns vision into form.",
    "Chitra":            "Brilliant, creative, and architecturally gifted. Chitra is the bright jewel — those with planets here have an eye for beauty and an instinct for creating structures and aesthetics that last. There is magnetism and a desire to be seen.",
    "Swati":             "Independent, wind-like, and adaptable. Swati is the young sprout that bends in the storm but does not break. There is a strong need for freedom, an instinct for trade and diplomacy, and the ability to spread ideas widely.",
    "Vishakha":          "Purposeful, patient, and determined. The triumphal arch of Vishakha stands at the threshold of achievement. Those with planets here pursue their goals with single-minded dedication — they may sacrifice much, but they rarely stop short of the destination.",
    "Anuradha":          "Devoted, disciplined, and capable of great friendship. Anuradha carries the energy of Mitra — divine friendship and alliance. There is a talent for loyalty, organization, and working with others toward shared sacred goals.",
    "Jyeshtha":          "Senior, protective, and intensely capable. Jyeshtha is the eldest — carrying responsibility, power, and sometimes isolation. There is an instinct to protect and lead that can become controlling; the wisdom is to protect without possessing.",
    "Mula":              "Rooting, investigating, and transformative. Mula means 'root' — it digs toward the foundational truth of any matter. This nakshatra carries enormous spiritual potential alongside the capacity for upheaval and radical dissolution of the old.",
    "Purva Ashadha":     "Invincible, purifying, and visionary. The fan of Purva Ashadha clears the air before the battle is declared. There is an unwillingness to admit defeat and a visionary quality that sees the destination before the path is fully known.",
    "Uttara Ashadha":    "Universal, victorious, and long-suffering. Where Purva Ashadha declares, Uttara Ashadha completes. There is a quality of final victory here — earned through patience, endurance, and a commitment to principles over convenience.",
    "Shravana":          "Listening, learning, and spiritually receptive. The ear of Shravana carries the capacity to receive wisdom from all directions. Those with planets here learn through listening, have extraordinary retention, and often carry knowledge that heals.",
    "Dhanishtha":        "Rhythmic, abundant, and communal. The drum of Dhanishtha calls the community together. There is musical intelligence here, a love of abundance, and the ability to gather resources and people toward shared celebration and creation.",
    "Shatabhisha":       "Healing, mysterious, and solitary. The empty circle of Shatabhisha contains multitudes. There is deep healing ability, a fascination with the occult and scientific mysteries, and a need for solitude to process what the many rivers of perception bring.",
    "Purva Bhadrapada":  "Fierce, visionary, and transformative. The sword of Purva Bhadrapada cuts through comfort into truth. There is a quality of righteous intensity here — the capacity to sacrifice for principle and to see beyond ordinary human concerns.",
    "Uttara Bhadrapada": "Wise, compassionate, and deeply oceanic. The serpent in the deep water of Uttara Bhadrapada carries ancient wisdom, selfless devotion, and the capacity to hold vast inner worlds without being overwhelmed. The deepest wisdom is here.",
    "Revati":            "Gentle, abundant, and spiritually complete. The fish of Revati swim in the ocean of cosmic love. This is the final nakshatra — carrying the accumulated wisdom of all 26 before it. There is compassion, artistic sensitivity, and a soul nearing completion.",
}


def get_nakshatra_info(idx):
    return NAKSHATRAS[idx % 27]


# ── Planetary Interpretations ─────────────────────────────────────────────────

INTERPRETATIONS = {
    "Sun": {
        "Aries": "You carry a pioneering flame — your identity thrives on action, initiative, and forging new paths. There is a courageous directness to how you move through life, and others feel your magnetic willpower immediately. You are at your best when leading something, not following behind another's vision. Growth comes when you balance boldness with patience and learn to complete what you begin. The fire you carry is real — the challenge is learning to sustain it through the long middle of any endeavor, not just the exciting beginning.",
        "Taurus": "Your sense of self is rooted in the physical world — in beauty, sensory pleasure, and the slow accumulation of what endures. You build identity through steadfast effort and an unshakeable loyalty to your values. There is a quiet power in you that others recognize as reliability and integrity. The challenge is releasing attachment when circumstances demand change — your strength becomes a limitation when it curdles into stubbornness. When you allow yourself to evolve while maintaining your essential groundedness, your endurance becomes legendary.",
        "Gemini": "You are a natural communicator and intellectual shapeshifter, finding identity in ideas, curiosity, and connection. Your mind is quick and restless, forever drawn to the next fascinating thread. You are most alive in conversation — when ideas spark between people and the exchange of perspectives opens new worlds. Learning to commit fully to a direction channels your brilliant versatility into real impact. The invitation of your lifetime is to discover that depth and breadth are not opposites — the person who goes far AND deep is unstoppable.",
        "Cancer": "Your identity is woven through the heart — through family bonds, emotional memory, and the impulse to nurture. You lead with intuition and carry the emotional history of those you love as a kind of internal compass. Your sensitivity is not a weakness; it is an advanced form of intelligence that most people never develop. True strength emerges when you learn to offer the same tender care to yourself that you so freely give to others. The protective shell you sometimes retreat into is not your limitation — it is the container that allows your enormous depth to develop.",
        "Leo": "You were born to express and illuminate. Your identity is tied to creativity, generosity, and the authentic radiance that comes when you stop performing and simply shine. There is a warmth in you that draws people closer — not the heat of ego, but the genuine light of someone who cares. Power lives in vulnerability — the more genuinely you show up, the more magnetic you become. Your invitation is to distinguish between approval and love, and to discover that the greatest expression of your solar energy is giving light freely without needing it reflected back.",
        "Virgo": "Your identity finds meaning through service, precision, and the quiet mastery of craft. You are a natural analyst with an eye for what needs refinement and the discipline to do the work. The world may not always see the invisible labor you contribute, but over time your excellence speaks for itself. Growth comes in learning that your worth is not contingent on perfect execution. You are enough before the task is done.",
        "Libra": "You define yourself through relationship, harmony, and the pursuit of fairness. You have a natural aesthetic intelligence and a gift for seeing all sides of any situation. Cultivating a strong inner voice ensures your peacemaking doesn't become self-erasure. Your most powerful contribution comes when you are willing to name the imbalance, not just smooth it over.",
        "Scorpio": "Your identity is shaped by depth, intensity, and the relentless drive to uncover truth beneath the surface. You have an extraordinary capacity for transformation — you can rebuild yourself and others from the ruins. The work is learning to trust vulnerability as the gateway to real intimacy — the armor that kept you safe eventually becomes the thing that keeps love out. Transformation is your natural state; surrendering to it is your path.",
        "Sagittarius": "You are a seeker by nature — your identity expands through philosophy, travel, and the bold pursuit of meaning. An innate optimism and love of freedom fuel your journey, and you inspire others with your vision of possibility. Staying grounded in the present keeps your grand ideals from escaping into abstraction. The invitation is to be the embodiment of the wisdom you seek, not just the perpetual seeker.",
        "Capricorn": "You carry the soul of the builder — patient, purposeful, and willing to climb any mountain for what matters. Your identity is forged through integrity and long-haul effort, and the respect you earn is genuine and lasting. Allow rest and play as essential parts of the climb, not rewards you must earn. The full expression of your power includes knowing when to stop and enjoy the view.",
        "Aquarius": "Your identity is inseparable from your ideals. You think in systems, challenge conventions, and often sense the future before others do. The integration of heart and mind — learning to feel as well as analyze — unlocks your greatest capacity for real-world transformation. The visionary who can also be moved, and who moves others, is the most powerful version of Aquarius.",
        "Pisces": "You experience identity as something fluid, boundless, and spiritually charged. Your compassion, imagination, and sensitivity to the unseen world are rare gifts. The practice of healthy boundaries and discernment helps you remain a vessel of healing rather than absorbing others' pain as your own. Your most powerful contribution is allowing your extraordinary sensitivity to be fully expressed in a form the world can receive.",
    },
    "Moon": {
        "Aries": "Emotionally, you react quickly and passionately — feeling something fully before moving to the next experience. You need independence and space to process your inner world without being told how to feel. Your emotional courage is remarkable. Vulnerability without armor is your growth edge — the moment you allow someone to see your softness is usually the moment the connection deepens most.",
        "Taurus": "You find emotional security in consistency, comfort, and the familiar rituals of daily life. When the world feels unstable, you anchor yourself in the body — in good food, nature, and touch. Your emotional endurance is remarkable: you stay, you tend, you persist when others have moved on. The paradox is that the security you seek is ultimately internal — and the practices of grounding you already know are the path to finding it.",
        "Gemini": "Your inner world is a constant conversation — ideas, feelings, and perceptions weaving together in rapid succession. You process emotions through talking, writing, and making sense of what you feel intellectually. Stillness and direct emotional contact are the practices that bring your restless inner life to rest. The moment you stop narrating your feelings and simply allow them is often the most healing.",
        "Cancer": "The Moon in its own sign makes you extraordinarily attuned to emotional currents — your own and everyone else's. Home, belonging, and emotional safety are not luxuries for you; they are necessities. Your intuition is one of your most reliable navigational tools — trust what you sense even when you can't articulate it. Learning to set loving limits protects the deep well of care you carry.",
        "Leo": "You need your feelings to be seen and validated — not dismissed or minimized. Warmth, creativity, and heartfelt connection nourish your emotional world. When you feel secure, your generosity and emotional expressiveness become a gift to everyone around you. The inner work is learning that being seen and being loved are related but not identical.",
        "Virgo": "You process emotions through analysis and a desire to make yourself useful. Worry and self-criticism can masquerade as emotions — learning to distinguish anxiety from genuine feeling is key. When you offer yourself the same gentle, helpful care you give others, your inner world finds a peace that the constant self-improvement project cannot provide.",
        "Libra": "You need beauty, harmony, and relational balance to feel emotionally at ease. Conflict and injustice register deeply in your nervous system. Developing the capacity to face discomfort without smoothing it over prematurely is a powerful emotional skill. Genuine peace is richer than the absence of conflict.",
        "Scorpio": "Your emotional depths are vast and rarely fully visible to others. You feel with extraordinary intensity and have little tolerance for superficiality. Trust is sacred to you; once established, your loyalty is unwavering. Learning to release as naturally as you hold on brings liberation — the tidal quality of your emotional life is not a flaw to fix but a cycle to honor.",
        "Sagittarius": "You need emotional freedom — the sense that you can always find meaning, expand, and explore. Heavy emotional obligation or claustrophobic environments deplete you quickly. Philosophy, humor, and travel restore your inner fire when life feels too small. The invitation is to remain present in the full range of emotional experience rather than escaping upward into optimism before the feeling is complete.",
        "Capricorn": "You tend to process emotions privately, often channeling feelings into productivity or stoicism. There is a quiet resilience in you — you bear difficulty without complaint. True emotional healing comes when you allow yourself to be comforted rather than only enduring. Your emotional maturity tends to deepen with age, and many of your most tender chapters are still ahead.",
        "Aquarius": "You experience emotions with some detachment — observing them from a slight distance. You care deeply about humanity in the abstract and need intellectual stimulation to feel emotionally alive. Practicing presence in intimate, one-on-one connections deepens your emotional life in ways that group engagement cannot fully provide.",
        "Pisces": "Your emotional world is oceanic — boundless, empathic, and suffused with imagination and sensitivity. You absorb the moods of your environment effortlessly. Creative practice, solitude, and spiritual connection are your essential emotional anchors — not indulgences but necessities. The capacity for compassion you carry is extraordinary; the discernment of who and what deserves it is your lifelong refinement.",
    },
    "Mercury": {
        "Aries": "Your mind is fast, direct, and unafraid to say exactly what it thinks. You are a natural initiator of ideas and excel at cutting through complexity. Slowing down to listen fully and consider before speaking sharpens your natural intellectual boldness and prevents the collateral damage of words fired too quickly.",
        "Taurus": "You think deliberately and practically, preferring to process new information thoroughly before forming an opinion. Once you have made up your mind, your conviction is formidable. Exposure to new perspectives keeps your well-grounded thinking from calcifying into stubbornness.",
        "Gemini": "Mercury at home in Gemini gives you a quicksilver, wide-ranging intellect. You learn by connecting disparate ideas and thrive in fast-moving conversations. The key to depth is choosing a thread and following it all the way through.",
        "Cancer": "Your mind is intuitive and associative — you absorb information through feeling as much as logic. Memory is extraordinary, especially for emotionally charged experiences. Developing trust in your gut-level intelligence alongside analytical thinking gives you a powerful dual knowing.",
        "Leo": "You communicate with flair, warmth, and a natural sense of drama that draws people in. Your ideas are bold and creative, and you speak with a conviction that makes others want to believe what you believe. Remaining open to alternative viewpoints ensures your confident style doesn't shade into inflexibility.",
        "Virgo": "Your mind is analytical, discerning, and attentive to detail in ways that others miss entirely. You excel at problem-solving, editing, and finding more efficient pathways through complexity. Trusting the big picture alongside the details allows your exceptional precision to serve greater vision.",
        "Libra": "You think in terms of relationship, balance, and nuance — always weighing multiple perspectives before reaching a conclusion. This makes you a skilled mediator and fair-minded thinker. Developing decisiveness ensures your thoroughness doesn't become perpetual indecision.",
        "Scorpio": "Your mind goes straight to the hidden layer — you are drawn to what is concealed, unspoken, or psychologically complex. Research, investigation, and deep inquiry come naturally. Learning to trust others with your insights builds the collaborative power that matches your lone-investigator brilliance.",
        "Sagittarius": "You think in big patterns and long arcs — always looking for the philosophical framework beneath the facts. Your enthusiasm for ideas is infectious. Practicing precision and follow-through gives your visionary thinking the grounding it needs to become real.",
        "Capricorn": "Your mind is strategic, structured, and long-range in its orientation. You excel at planning, organizing, and identifying the most efficient path to a goal. Allowing creative and intuitive inputs to influence your structured thinking keeps your intellect fresh.",
        "Aquarius": "You are a genuinely original thinker — your mind sees patterns and possibilities that conventional frameworks miss. You are drawn to systems thinking and ideas that challenge the status quo. Staying connected to the human impact of your ideas grounds your brilliance in real-world relevance.",
        "Pisces": "Your mind is poetic, associative, and attuned to subtlety. You think in metaphors and images as often as in logical sequences, and your imagination is a genuine cognitive tool. Developing clear structures for communicating your insights helps others access the beauty of how you perceive the world.",
    },
    "Venus": {
        "Aries": "In love, you are passionate, direct, and electric — you pursue what you want with refreshing honesty and zero pretense. Relationships need to feel alive and exciting. Learning to tend the steady flame once the initial spark ignites creates the lasting love you also crave beneath the thrill-seeking.",
        "Taurus": "Venus in Taurus — the sign she rules — makes you deeply sensual, loyal, and devoted in love. You value security, physical affection, and a partner you can build with over time. Remaining open when things don't unfold at your preferred pace protects your relationships from unnecessary rigidity.",
        "Gemini": "You are drawn to wit, intelligence, and someone who can hold a conversation at any hour. Variety and mental stimulation keep your love life vibrant. Allowing emotional depth to develop alongside intellectual chemistry creates the full-spectrum connection you didn't know you needed.",
        "Cancer": "Love for you is sanctuary — you cherish emotional intimacy, domestic warmth, and a relationship that feels like home. Your care and devotion run very deep. Learning to express your needs directly, rather than hoping they'll be intuited, transforms your relationships.",
        "Leo": "You love with a full, generous, theatrical heart — gifts, attention, and grand gestures of appreciation come naturally. You need to be seen, celebrated, and admired in return. When the mutual adoration is authentic, you are one of the most devoted and joyful partners in any zodiac.",
        "Virgo": "You show love through acts of service — noticing what needs doing and doing it without being asked. Your devotion is real and expressed practically. Softening your inner critic in relationship allows the warmth beneath your precision to flow freely.",
        "Libra": "Venus in her home sign of Libra makes you a natural romantic — gracious, aesthetically attuned, and deeply committed to partnership. You seek beauty, balance, and a true meeting of equals. Developing the capacity to disagree without destabilizing the relationship is your growth edge.",
        "Scorpio": "Love for you is total — an all-or-nothing dive into depth, loyalty, and transformation. You can sense the authenticity of a connection instantly. Learning to let trust build over time, rather than testing for it through intensity, creates the profound union you are capable of.",
        "Sagittarius": "You fall for freedom, adventure, and someone who expands your world. Relationships need to breathe — room for individual growth and philosophical conversations into the night. A partner who is also a fellow traveler is your ideal.",
        "Capricorn": "You take love seriously and are drawn to partners with substance, integrity, and ambition. You may be reserved in early courtship, but your devotion once committed is enduring and unshakeable. Allowing vulnerability and play into your relationship reveals the profound tenderness beneath.",
        "Aquarius": "You are attracted to originality, intelligence, and someone who sees the world differently than most. Friendship is the foundation of your best romantic connections. Letting yourself be fully emotionally present, rather than observing from a slight distance, opens the doors to profound intimacy.",
        "Pisces": "Your love is boundless, imaginative, and deeply spiritual — you fall for the soul. You are capable of extraordinary devotion and empathy in relationship. Developing discernment about who deserves your oceanic love protects your tender heart while keeping it open.",
    },
    "Mars": {
        "Aries": "Mars in its home sign gives you an instinctive, high-octane drive. You act first and think second, which makes you a natural trailblazer. Channeling your fierce energy into sustained effort transforms your extraordinary spark into enduring achievement.",
        "Taurus": "Your drive is patient, persistent, and phenomenally determined — once you set a goal, almost nothing stops you. You build slowly but to last. Remaining flexible when faster pivots would serve you keeps your impressive tenacity from becoming an anchor.",
        "Gemini": "You are driven by curiosity — your energy ignites around ideas and the thrill of learning something new. You pursue multiple projects simultaneously. Choosing where to concentrate your fire produces greater results than spreading it evenly.",
        "Cancer": "Your drive is deeply emotional — you are most motivated when fighting for those you love or protecting what feels like home. Your fiercely protective streak surprises people who mistook your gentleness for passivity. Recognizing when defensiveness is armor and when it is wisdom keeps your protective instincts healthy.",
        "Leo": "Your desire is creative, proud, and driven by the need to make a meaningful mark. You pour extraordinary energy into everything you put your name on. Leading by inspiration rather than domination lets your natural magnetism work in full.",
        "Virgo": "You channel your drive into mastery, service, and the satisfaction of doing difficult things exceptionally well. Your work ethic is formidable and your attention to quality sets you apart. Releasing the perfectionism that sometimes prevents you from starting allows your diligence to find its full expression.",
        "Libra": "You are motivated by fairness, beauty, and the creation of harmony. You can be surprisingly tenacious in pursuit of equity once you have decided a cause is worth fighting for. Finding comfort with healthy conflict ensures your diplomatic nature doesn't leave your own needs unmet.",
        "Scorpio": "Mars in Scorpio is relentless and strategic — you pursue your goals with laser focus and an extraordinary capacity to endure. You do not give up. Ensuring your formidable will serves regeneration rather than control or revenge is the central practice. When your power serves transformation, you are genuinely unstoppable.",
        "Sagittarius": "Your drive is propelled by vision, freedom, and the thirst for meaning — you need to believe in what you're pursuing. You take inspired, courageous action toward possibilities that excite you. Pairing your expansive energy with follow-through gives your ambitions the structural grounding to become real.",
        "Capricorn": "Mars is exalted in Capricorn — your ambition is disciplined, long-range, and quietly relentless. You work harder than most and take immense satisfaction in climbing the mountain through your own effort. Rest is not weakness; it is part of the strategy.",
        "Aquarius": "You are driven by ideas, causes, and the desire to create something genuinely new. Your energy is most alive when directed toward collective change or innovative breakthroughs. Patience with the pace of others allows your visionary drive to build real coalitions.",
        "Pisces": "Your drive flows in currents rather than straight lines — you are moved by inspiration, compassion, and intuition. When connected to a meaningful cause, your quiet persistence surprises those who underestimated your softness. Clear intention and structure give your fluid energy a channel to flow powerfully through.",
    },
    "Jupiter": {
        "Aries": "Jupiter expands your capacity for bold action, leadership, and entrepreneurial vision. You attract abundance when you take courageous initiative and trust your pioneering instincts. The more authentically you lead, the more opportunities arise.",
        "Taurus": "Your path to abundance runs through patience, sensory appreciation, and building material and spiritual resources over time. You attract wealth through steady effort and by honoring what is genuinely valuable. Gratitude and embodied pleasure are your expansion keys.",
        "Gemini": "You grow through communication, learning, and the joyful exchange of ideas. Teaching, writing, and connecting people and concepts expand your world significantly. The more widely you share your knowledge, the more fortune flows back to you.",
        "Cancer": "Expansion comes through emotional intelligence, family bonds, and honoring your intuitive gifts. Your capacity to nurture creates a legacy of loyalty and belonging. Home, heritage, and emotional wisdom are genuine sources of abundance.",
        "Leo": "Jupiter amplifies your natural creativity, generosity, and desire to be seen in full. You grow through self-expression, performance, and the authentic sharing of your gifts. The universe rewards your genuine heartfulness — the more openly you give, the more you receive.",
        "Virgo": "You grow through service, skill development, and the relentless refinement of your craft. Meaningful work and genuine helpfulness bring abundance. Knowing when enough is enough allows you to enjoy the fruits of your extraordinary diligence.",
        "Libra": "Partnership, aesthetic pursuits, and the cultivation of fairness are your expansion avenues. You attract good fortune through collaboration and by creating beauty and harmony. Your relationships are among your greatest teachers and most significant sources of growth.",
        "Scorpio": "You grow through deep transformation, psychic development, and your willingness to go where others fear. Your capacity to regenerate after loss is a genuine superpower. The deeper you are willing to go, the more Jupiter rewards you.",
        "Sagittarius": "Jupiter in its home sign — your wisdom, optimism, and philosophical breadth are gifts you carry into the world with unusual power. Higher education, travel, and publishing expand your life significantly. Your faith in something larger than yourself is both contagious and generative.",
        "Capricorn": "You grow through disciplined pursuit of long-term goals and the patient building of lasting structures. Success comes through integrity and earned authority. Your most expansive chapters often arrive later, built on foundations you laid when no one was watching.",
        "Aquarius": "You expand through innovation, group collaboration, and visionary thinking that challenges the status quo. Collective endeavors and humanitarian causes are genuine vehicles for your abundance. Your Jupiter grows largest when you pursue it in service of something larger than personal gain.",
        "Pisces": "Jupiter is at home in Pisces — your compassion, spiritual sensitivity, and imaginative depth are genuine abundance generators. Art, spirituality, healing, and inner wisdom are your portals to growth. The more you trust your intuition and serve something larger, the more life provides.",
    },
    "Saturn": {
        "Aries": "Saturn in Aries asks you to develop authentic self-authority — earned through facing fear and acting anyway, not through aggression. Your greatest accomplishments come when you harness your initiative within a disciplined framework.",
        "Taurus": "Your Saturn lessons center on building genuine security through slow, steady effort rather than clinging to comfort. You are learning that true stability is internal. Developing flexibility alongside your admirable persistence creates unshakeable groundedness.",
        "Gemini": "Saturn in Gemini asks you to develop disciplined thinking — to go deep rather than wide, and to communicate with precision and earned authority. Writing, teaching, or mastering a specific body of knowledge is your Saturn path.",
        "Cancer": "Your life lessons involve emotional boundaries, healthy family patterns, and learning to receive care as well as give it. The healing comes through allowing vulnerability and building the emotional safety you always deserved.",
        "Leo": "Saturn in Leo teaches you authentic self-expression — the kind that doesn't require external validation. Your most powerful work emerges when you create from genuine inner authority rather than performance or approval-seeking.",
        "Virgo": "Your Saturn lessons involve releasing perfectionism and learning to value yourself as you are, not only as you produce. True mastery means knowing when something is complete — and letting it be.",
        "Libra": "Saturn in Libra — its exaltation — asks you to build relationships on genuine equality and integrity. You are learning that real harmony requires the courage to address imbalance directly. Your relationship lessons forge your strongest qualities.",
        "Scorpio": "Your Saturn lessons involve power — learning to use it with integrity, release control, and transform without destruction. Your capacity for regeneration is extraordinary when you stop fighting change and begin working with it.",
        "Sagittarius": "Saturn in Sagittarius asks you to develop an earned, tested philosophy — one forged through real experience, not inherited belief. True wisdom comes when you hold convictions lightly enough to keep learning.",
        "Capricorn": "Saturn at home — you carry a natural understanding of effort, responsibility, and the long game. The lesson is to work toward what genuinely matters to you, not only what you believe you should achieve. Your ambition, guided by heart, is extraordinary.",
        "Aquarius": "Saturn in Aquarius asks you to develop the discipline of original thinking — to build something genuinely new rather than merely rebelling against the old. Structure and vision working together is your unique gift.",
        "Pisces": "Saturn in Pisces asks you to develop healthy boundaries around your sensitivity and compassion. You are learning to be grounded and present even while remaining open to the unseen. Creative or healing disciplines give your spiritual nature a form that endures.",
    },
    "Uranus": {
        "Aries": "Your generation brings sudden, revolutionary change to how identity, leadership, and courage are expressed. Innovation and independence are your generation's watchwords.",
        "Taurus": "Your generation is fundamentally disrupting humanity's relationship with material resources, land, the body, and the natural world. What you build is meant to endure — but in a new form.",
        "Gemini": "Your generation reshapes communication, media, education, and the way information moves through the world. You are wired to think outside every known category.",
        "Cancer": "Your generation challenges traditional family structures, homeland, and emotional norms. The definition of home and belonging is being radically reimagined by your cohort.",
        "Leo": "Your generation disrupts the nature of creativity, self-expression, and leadership. New art forms and revolution in how we celebrate the self are your collective hallmarks.",
        "Virgo": "Your generation revolutionizes health, daily work, and service systems. Radical reinvention of medicine, wellness, and the relationship between humans and labor define your cohort's impact.",
        "Libra": "Your generation upends the structures of relationship, justice, and aesthetic culture. You are collectively building a new framework for what genuine equality actually looks like.",
        "Scorpio": "Your generation radically transforms the deepest domains — death, sexuality, power, and hidden resources. Power dynamics in all their forms are your generation's obsession and transformation.",
        "Sagittarius": "Your generation challenges the existing structures of belief — religion, higher education, and what it means to seek meaning. Your cohort rewrites the map of human possibility.",
        "Capricorn": "Your generation disrupts institutions, governments, and corporate power. Building something genuinely new from the rubble of what no longer serves is your generational calling.",
        "Aquarius": "Uranus in its own sign — your generation embodies the Aquarian revolution at full voltage, rewiring the very network of civilization.",
        "Pisces": "Your generation dissolves boundaries in spirituality, art, imagination, and the collective unconscious. New forms of collective healing and transcendence are emerging through your generation's sensitivity.",
    },
    "Neptune": {
        "Aries": "A rare placement that brings spirituality and idealism into contact with raw, pioneering energy. The spiritual warrior archetype — inspired action for a transcendent cause — may be one expression of this energy.",
        "Taurus": "Neptune in Taurus blends the spiritual with the material — dissolving the boundary between the earthly and the sacred. Art, nature, and the spiritual dimension of physical reality are your collective portals.",
        "Gemini": "Your generation dissolves fixed ideas through the magical power of language, story, and interconnection. The blurring of fact and fiction and the spiritualization of communication are your generational themes.",
        "Cancer": "Your generation experiences Neptune's dissolving influence through family, homeland, and emotional memory. Spiritual connection through ancestry, home, and care is a deep current.",
        "Leo": "The spiritualization of creativity, performance, and the heart — your generation dissolves the boundary between art and transcendence. True creativity as a spiritual act is your cohort's invitation.",
        "Virgo": "Your generation experiences Neptune as a dissolution of separation between service and spiritual devotion. Healing, medicine, and care become mystical callings. The boundaries between practical service and sacred practice blur beautifully.",
        "Libra": "Your generation dissolves the hard edges of relationship — dreaming of ideal partnership and a more just and harmonious world. Compassionate relationship as a spiritual path is the invitation.",
        "Scorpio": "Your generation dissolves the veil between the living and the dead, the conscious and the unconscious. Depth psychology, occult exploration, and the collective confrontation with power and transformation are your Neptune-in-Scorpio themes.",
        "Sagittarius": "Your generation dreams of universal truth — a spirituality beyond all dogma. The dissolution of rigid religious structures and the explosion of spiritual seeking in all directions define your cohort.",
        "Capricorn": "Your generation brings spiritual idealism into contact with the structures of authority and ambition. The dream of institutions with genuine integrity is your Neptune-in-Capricorn longing.",
        "Aquarius": "Your generation dissolves the boundaries of the individual self in service of collective awakening. Spiritual community, technological oneness, and the dissolution of separation between self and humanity are your collective themes.",
        "Pisces": "Neptune at home — your generation carries extraordinary sensitivity, spiritual porousness, and collective empathy. The boundary between the individual and the whole is at its most transparent.",
    },
    "Rahu": {
        "Aries": "Rahu in Aries drives you toward bold self-assertion, leadership, and the courage to forge your own path without apology. Your dharma this lifetime involves taking action first, refining later — the hesitation that kept you safe in past lives is now the very thing holding you back. Embrace the pioneer within.",
        "Taurus": "Rahu in Taurus draws you toward material security, sensory beauty, and the patient accumulation of real-world resources. Your dharma involves learning to trust the physical world — to build, to own, to enjoy — without the spiritual guilt that may have kept you from abundance in other lifetimes. Wealth and beauty are valid spiritual expressions.",
        "Gemini": "Rahu in Gemini pulls you toward the world of ideas, communication, and endlessly curious engagement with others. Your dharma involves learning to think in new frameworks, to speak your truth publicly, and to exchange knowledge as a form of contribution. The lone mystic of past lives is being asked to join the conversation.",
        "Cancer": "Rahu in Cancer draws you toward emotional intimacy, family bonds, and the nurturing of what is tender and vulnerable. Your dharma involves learning to need — to accept belonging and to risk the vulnerability of genuine attachment. The past life wanderer is being called home.",
        "Leo": "Rahu in Leo pulls you toward creative self-expression, recognition, and the courageous act of standing in your own light. Your dharma involves learning to be seen — to lead, to create, and to accept the attention your soul actually craves without the self-effacement that belonged to other lifetimes.",
        "Virgo": "Rahu in Virgo draws you toward service, discernment, and the mastery of practical skills. Your dharma involves learning to work — to be useful in concrete, day-to-day ways — and to find spiritual meaning in the details of ordinary life. The mystic must learn to wash the dishes with full presence.",
        "Libra": "Rahu in Libra pulls you toward partnership, aesthetic refinement, and the practice of genuine diplomacy. Your dharma involves learning to collaborate, to compromise, and to create beauty through relationship. The solitary seeker of past lives is being asked to discover the divine in the face of another.",
        "Scorpio": "Rahu in Scorpio draws you toward depth, transformation, and the radical exploration of power and the hidden self. Your dharma involves confronting what lies beneath the surface — psychologically, spiritually, and materially. The deeper you go, the more powerful and purposeful your life becomes.",
        "Sagittarius": "Rahu in Sagittarius pulls you toward philosophy, higher education, travel, and the expansion of worldview that comes from genuine cross-cultural encounter. Your dharma involves developing a real and tested faith — not inherited but earned through experience that stretches you beyond your origin story.",
        "Capricorn": "Rahu in Capricorn draws you toward ambition, authority, and the construction of something lasting in the world. Your dharma involves learning to work within structures — to build an institution, a career, or a legacy — without the spiritual bypassing that kept you from worldly engagement in past lives.",
        "Aquarius": "Rahu in Aquarius pulls you toward collective causes, innovation, and the visionary ideas that serve humanity rather than just the self. Your dharma involves joining the larger current of human evolution — to think beyond the tribe, to work with the network, and to build systems that outlast you.",
        "Pisces": "Rahu in Pisces draws you toward spiritual surrender, mystical experience, and the dissolution of the ego's grip on what it thinks it controls. Your dharma involves learning to trust the unseen — to let go, to dream, to serve without needing credit — and to discover the liberation that waits on the other side of surrender.",
    },
    "Ketu": {
        "Aries": "Ketu in Aries indicates past mastery of self-assertion, independence, and physical courage. The soul has already lived fully in the warrior's skin. Now you are called away from aggressive self-interest toward something that serves others — the fire that once burned for the self must become warmth for the collective.",
        "Taurus": "Ketu in Taurus suggests past mastery of material security, sensory comfort, and the pleasures of earthly life. The soul knows how to accumulate — now it is called to release, to simplify, and to discover the wealth that cannot be owned. A natural detachment from material excess is both gift and spiritual calling.",
        "Gemini": "Ketu in Gemini indicates past mastery of communication, intellectualism, and social exchange. The mind has already gathered enormous knowledge over many lifetimes. Now you are called toward depth over breadth — toward silence, meditation, and the wisdom that cannot be spoken, only experienced.",
        "Cancer": "Ketu in Cancer suggests past mastery of family bonds, emotional protection, and the art of belonging. The soul has lived deeply in the web of attachment. Now you are called toward a love that transcends biology — toward compassion for all beings rather than only your kin.",
        "Leo": "Ketu in Leo indicates past mastery of creative self-expression, leadership, and the experience of being recognized and celebrated. The soul has stood in the spotlight. Now you are called toward the service of something greater than personal glory — your genius finds its purest expression when given freely.",
        "Virgo": "Ketu in Virgo suggests past mastery of craft, service, and the perfection of daily practice. The soul has already refined itself through discipline. Now you are called toward an expansive trust in the larger pattern — to stop micromanaging the universe and to discover that not all things need to be fixed.",
        "Libra": "Ketu in Libra indicates past mastery of relationship, diplomacy, and the careful maintenance of social harmony. The soul knows how to partner. Now you are called toward an individual wholeness that doesn't require a counterpart — the liberation of the self that is complete without needing to be paired.",
        "Scorpio": "Ketu in Scorpio suggests past mastery of depth, occult knowledge, and the experience of extreme transformation. The soul has descended and returned. Now you are called to bring that knowledge back to the surface — to use what you have survived as a light for others, rather than retreating into the depths alone.",
        "Sagittarius": "Ketu in Sagittarius indicates past mastery of philosophy, religious practice, and the seeking of ultimate truth. The soul has walked the path of the teacher and the pilgrim. Now you are called toward the grounded application of wisdom — not seeking but serving, not traveling but arriving, again and again, in the present moment.",
        "Capricorn": "Ketu in Capricorn suggests past mastery of ambition, authority, and institutional achievement. The soul has built empires in other times. Now you are called toward something that cannot be measured by worldly success — toward the authority that comes from spiritual rather than social elevation.",
        "Aquarius": "Ketu in Aquarius indicates past mastery of collective ideals, revolutionary ideas, and the role of the visionary outsider. The soul has already tried to change the world. Now you are called toward the intimate — toward the personal, the warm, the embodied — to discover that the revolution begins in a single, present moment of genuine connection.",
        "Pisces": "Ketu in Pisces suggests past mastery of spiritual surrender, mystical absorption, and the dissolution of personal boundaries. The soul has touched the infinite. Now you are called back into form — to bring what you found in the formless into practical, compassionate expression in the world of ordinary experience.",
    },
    "Ascendant": {
        "Aries": "With Aries rising, you meet the world with energy, directness, and an unmistakable forward momentum. People experience you as confident, decisive, and sometimes impatient — you give the impression of someone always ready to act. Your physical presence is often magnetic and your first impressions are bold.",
        "Taurus": "Taurus rising gives you an aura of calm solidity, beauty, and unhurried ease. People experience you as warm, dependable, and grounded — someone safe to stand beside. Your physical presence often carries an aesthetic quality, and your pace is deliberate and reassuring.",
        "Gemini": "With Gemini rising, you approach the world with curiosity, adaptability, and a quick, engaging wit. You seem youthful and multi-faceted to others — endlessly interested and interesting. Your ability to read and respond to any room makes you a natural connector.",
        "Cancer": "Cancer rising gives you an approachable, warm, and emotionally responsive presence. People feel instinctively comfortable with you — as if they can be cared for without judgment. Your protective instincts shape how you move through the world.",
        "Leo": "Leo rising gives you a radiant, warm, and unmistakably luminous presence. People notice you when you enter a room — not from showmanship, but from an inner warmth that is simply hard to ignore. You carry yourself with a natural dignity and creative flair.",
        "Virgo": "Virgo rising gives you an observant, precise, and quietly helpful presence. People experience you as thoughtful, detail-oriented, and someone who genuinely cares about getting things right. Your approach to life tends to be methodical and discerning.",
        "Libra": "Libra rising blesses you with natural grace, social ease, and aesthetic polish. People experience you as charming, fair-minded, and easy to be around. Your approach to life is always seeking balance, beauty, and some form of refined harmony.",
        "Scorpio": "Scorpio rising gives you an intense, perceptive, and magnetically private presence. People sense there is more beneath your surface than you reveal — which draws them in. Your gaze tends to go straight to what is real and unspoken in any situation.",
        "Sagittarius": "With Sagittarius rising, you approach life with optimism, philosophical curiosity, and an infectious enthusiasm for what might be possible. People experience you as inspiring, sometimes restless, and always oriented toward the horizon.",
        "Capricorn": "Capricorn rising gives you an air of quiet authority, composure, and measured competence. People may initially find you reserved, but come to rely on your consistency and integrity. You carry yourself with a mature dignity that commands respect.",
        "Aquarius": "Aquarius rising gives you an original, somewhat unusual, and distinctly individualistic presence. People experience you as intellectually fascinating, slightly unconventional, and friendly in a detached way. Your approach to life tends to be ahead of its time.",
        "Pisces": "Pisces rising gives you a gentle, dreamy, and empathic presence. People often feel immediately at ease with you — as if judgment has left the building. You absorb impressions and atmospheres effortlessly, with a quality of spiritual openness.",
    },
    "Midheaven": {
        "Aries": "Your public calling is one of courage and initiative — the world recognizes you as someone who leads from the front and makes things happen. Career fulfillment comes through pioneering, competing, and being the person in the room who decides rather than waits.",
        "Taurus": "Your public legacy is built through patience, quality, and the creation of lasting value. The world recognizes you as reliable, skilled, and someone whose work endures. Career fulfillment comes through craftsmanship, stewardship, and work connected to beauty, nature, or material substance.",
        "Gemini": "Your professional calling is inseparable from communication, ideas, and connection. The world recognizes you as a versatile, articulate, and mentally agile contributor. Career fulfillment comes through environments that reward curiosity, adaptability, and the exchange of information.",
        "Cancer": "Your professional legacy is rooted in care, emotional intelligence, and genuine service to others. The world recognizes you as someone whose work has real human impact. Career fulfillment comes through vocations that allow you to nurture, protect, or preserve something precious.",
        "Leo": "Your public destiny involves creative expression and authentic leadership. The world recognizes your radiance and capacity to inspire. Career fulfillment comes through environments where your creativity, personality, and vision are the product.",
        "Virgo": "Your professional legacy is built through mastery, precision, and the quiet excellence of doing things exceptionally well. The world recognizes you as indispensable, discerning, and someone whose standards elevate everything they touch.",
        "Libra": "Your professional calling is built through partnership, aesthetic intelligence, and the creation of harmony. The world recognizes you as gracious, fair-minded, and extraordinary in the art of human relationship.",
        "Scorpio": "Your public legacy is forged in the deep — in the transformative, the complex, and the high-stakes. The world recognizes you as formidable and capable of doing what others cannot.",
        "Sagittarius": "Your professional legacy is an ever-expanding horizon — a life built on the pursuit of truth, meaning, and the inspiration of others. The world recognizes you as a visionary, teacher, and philosophical guide.",
        "Capricorn": "Your professional destiny is inseparable from authority, integrity, and the construction of something that outlasts you. The world recognizes you as someone who means what they say and delivers on their commitments.",
        "Aquarius": "Your professional legacy belongs to the future — to ideas and systems that haven't fully arrived yet. The world recognizes you as a visionary who builds movements rather than monuments.",
        "Pisces": "Your professional legacy is woven from compassion, imagination, and the willingness to dissolve the boundary between work and soul. The world recognizes you as someone whose work comes from a different place — a genuine vocation.",
    },
}


def get_interpretation(planet, sign):
    planet_data = INTERPRETATIONS.get(planet, {})
    return planet_data.get(sign, f"{planet} in {sign} reflects a unique blend of planetary energy and sign qualities that manifests distinctly in your chart.")


# ── Career Section ────────────────────────────────────────────────────────────

CAREER_BY_SIGN = {
    "Aries":       {"professions": ["Entrepreneur / Startup Founder","Military Officer / Special Forces","Emergency Surgeon or Trauma Doctor","Professional Athlete or Sports Coach","Fire Fighter / Search & Rescue","Executive Director or CEO","Criminal Defense Attorney","Competitive Sales Director"],"mc_description": "With Midheaven in Aries, your public legacy is built on courage, initiative, and the willingness to go first when others hesitate. You are drawn to careers that reward bold action and decisive leadership. The world recognizes you as a trailblazer — someone who carves their own path rather than inheriting one. You thrive in high-stakes, fast-moving environments where there is no time to second-guess. Your professional peak arrives when you stop waiting for permission and start treating every obstacle as a signal to move faster.","work_strengths": ["Decisive under pressure","Natural leadership presence","High tolerance for risk and challenge","Entrepreneurial instinct","Motivates others through example"]},
    "Taurus":      {"professions": ["Financial Advisor or Investment Banker","Landscape Architect or Horticulturist","Chef or Restaurateur","Real Estate Developer","Fine Art Dealer or Appraiser","Interior Designer","Agricultural Business Owner","Voice Actor or Singer"],"mc_description": "With Midheaven in Taurus, your professional legacy is built through patience, quality, and the creation of lasting value. You are drawn to careers that reward craftsmanship, reliability, and tangible results. The world recognizes you as someone who builds to last. Beauty, nature, material substance, and financial integrity are natural domains.","work_strengths": ["Exceptional follow-through and persistence","Financial acumen and stewardship","Aesthetic sensibility and quality standards","Reliability and trustworthiness","Ability to create long-term value"]},
    "Gemini":      {"professions": ["Journalist or Investigative Reporter","Copywriter or Creative Director","Software Engineer","Publicist or Communications Strategist","Podcast Host or Media Personality","Educator or Curriculum Designer","Translator or Linguist","Market Research Analyst"],"mc_description": "With Midheaven in Gemini, your public calling is inseparable from communication, ideas, and the rapid movement of information. You are recognized in your field as someone who can translate complex ideas into accessible language. Versatility is your professional superpower.","work_strengths": ["Exceptional communication across mediums","Quick learning and adaptability","Networking and relationship-building","Multitasking and context-switching","Making complex ideas engaging and clear"]},
    "Cancer":      {"professions": ["Therapist or Counselor","Pediatrician or Neonatal Nurse","Social Worker","Chef or Catering Business Owner","Child Psychologist","Real Estate Agent (residential)","Historian or Archivist","Nonprofit Director"],"mc_description": "With Midheaven in Cancer, your professional legacy is rooted in care, emotional intelligence, and the desire to create safety and belonging for others. You are drawn to work that has human impact at its heart. The world recognizes you as someone who brings genuine warmth and emotional depth to their work.","work_strengths": ["Deep empathy and emotional attunement","Instinctive understanding of human needs","Loyalty and dedication to those in their care","Strong memory and preservation instinct","Creating environments where people feel safe"]},
    "Leo":         {"professions": ["Actor or Director","Creative Director or Brand Strategist","Fashion Designer","Motivational Speaker or Life Coach","Politician or Public Administrator","Luxury Brand Manager","Event Planner or Producer","School Principal or Educational Leader"],"mc_description": "With Midheaven in Leo, your public destiny involves creative expression, leadership, and the authentic use of your personal radiance as a professional tool. You are drawn to careers where you can be fully seen. The world recognizes you as someone with star quality and a gift for inspiring others.","work_strengths": ["Commanding, charismatic presence","Exceptional creative vision","Ability to inspire and energize others","Courage in self-expression and leadership","Generosity that builds loyal professional relationships"]},
    "Virgo":       {"professions": ["Physician or Specialist Surgeon","Data Scientist or Statistician","Editor or Technical Writer","Nutritionist or Functional Medicine Practitioner","Forensic Analyst","Quality Assurance Engineer","Accountant or Auditor","Research Scientist"],"mc_description": "With Midheaven in Virgo, your professional legacy is built through mastery, precision, and the quiet dignity of doing things exceptionally well. You are drawn to careers that require careful analysis, systematic thinking, and a commitment to excellence over spectacle. The world recognizes you as someone indispensable.","work_strengths": ["Unmatched attention to detail","Systematic, analytical problem-solving","High professional standards and reliability","Practical intelligence in complex situations","Commitment to continuous improvement"]},
    "Libra":       {"professions": ["Attorney or Judge","Diplomat or International Relations Specialist","Art Curator or Gallery Director","HR Director or Organizational Mediator","Wedding or Event Planner","Marriage & Family Therapist","Fashion Stylist or Beauty Industry Executive","Architect or Interior Designer"],"mc_description": "With Midheaven in Libra, your professional legacy is built through partnership, aesthetic intelligence, and the creation of harmony in places where it is absent. The world recognizes you as someone gracious, fair-minded, and extraordinarily skilled in the art of human relationships.","work_strengths": ["Exceptional negotiation and conflict resolution","Natural diplomatic intelligence","Aesthetic discernment and design sensibility","Building consensus and collaborative frameworks","Creating professional relationships built on mutual respect"]},
    "Scorpio":     {"professions": ["Psychiatrist or Trauma Therapist","Investigative Journalist or Intelligence Analyst","Forensic Psychologist","Surgeon or Oncologist","Detective or Criminal Profiler","Venture Capitalist or Private Equity Analyst","Research Scientist (cutting-edge domains)","Crisis Negotiator"],"mc_description": "With Midheaven in Scorpio, your professional legacy is forged in the deep — in the hidden, the complex, and the transformative. You are drawn to careers that require the courage to face what others turn away from. The world recognizes you as someone formidable with a penetrating intelligence.","work_strengths": ["Penetrating research and investigative acumen","Exceptional resilience under extreme pressure","Strategic thinking and psychological insight","Capacity to handle high-stakes, sensitive material","Transforming crises into breakthroughs"]},
    "Sagittarius": {"professions": ["University Professor or Academic","Travel Writer or Documentary Filmmaker","Philosopher or Cultural Theorist","Religious or Spiritual Leader","International Business Development Director","Attorney specializing in international law","Cross-cultural Consultant","Publisher or Literary Agent"],"mc_description": "With Midheaven in Sagittarius, your professional legacy is an ever-expanding horizon — a life built on the pursuit of truth, meaning, and the liberation that comes from genuine understanding. You are drawn to careers that reward vision, philosophical depth, and the ability to inspire others with a bigger picture.","work_strengths": ["Visionary thinking and big-picture strategic clarity","Inspiring others through enthusiasm and conviction","Cross-cultural understanding and adaptability","Synthesizing knowledge from diverse sources","Turning philosophical insight into practical guidance"]},
    "Capricorn":   {"professions": ["CEO or C-Suite Executive","Government Official or Elected Representative","Civil Engineer or Urban Planner","Investment Manager or CFO","Corporate Lawyer","University President or Academic Administrator","Military General or Senior Commander","Architect (large-scale institutional projects)"],"mc_description": "With Midheaven in Capricorn, your professional destiny is inseparable from authority, integrity, and the construction of something that outlasts you. You are drawn to careers where genuine mastery and earned respect are the currency. The world recognizes you as someone who means what they say and delivers on their commitments.","work_strengths": ["Exceptional long-term strategic planning","Unwavering professional integrity","Authority earned through demonstrated competence","Patience with the pace of institutional change","Building structures and legacies that endure"]},
    "Aquarius":    {"professions": ["Technology Entrepreneur or CTO","Social Activist or NGO Director","Scientist (theoretical physics, AI, systems biology)","Urban Futurist or Policy Designer","Software Architect","Humanitarian Aid Director","Documentary Filmmaker (social issues)","Academic Researcher in emerging fields"],"mc_description": "With Midheaven in Aquarius, your professional legacy belongs to the future — to ideas and systems that haven't fully arrived yet. You are drawn to careers that allow you to break convention, challenge outdated structures, and create something genuinely original in service of human progress.","work_strengths": ["Genuinely original and systemic thinking","Building collaborative networks and movements","Comfort with disruption and paradigm shifts","Long-range foresight and pattern recognition","Translating complex ideas into collective action"]},
    "Pisces":      {"professions": ["Musician, Composer or Sound Healer","Filmmaker or Visual Artist","Psychiatrist or Addiction Counselor","Spiritual Director or Contemplative Teacher","Marine Biologist or Oceanographer","Photographer or Cinematographer","Hospice Care Specialist","Dance or Movement Therapist"],"mc_description": "With Midheaven in Pisces, your professional legacy is woven from compassion, imagination, and the willingness to dissolve the boundary between your work and your soul. You are drawn to careers that involve healing, art, spiritual practice, or service to the most vulnerable.","work_strengths": ["Deep empathy and healing presence","Extraordinary imagination and artistic sensitivity","Ability to access and express the ineffable","Spiritual intelligence and intuitive perception","Inspiring others through beauty, story, and compassion"]},
}


def get_career_reading(placements):
    mc_sign      = placements.get("Midheaven", {}).get("sign")
    sun_sign     = placements.get("Sun",       {}).get("sign")
    jupiter_sign = placements.get("Jupiter",   {}).get("sign")
    saturn_sign  = placements.get("Saturn",    {}).get("sign")

    mc_data       = CAREER_BY_SIGN.get(mc_sign, {})
    professions   = mc_data.get("professions", [])
    mc_description = mc_data.get("mc_description", "")
    work_strengths = mc_data.get("work_strengths", [])

    jupiter_data     = CAREER_BY_SIGN.get(jupiter_sign, {})
    jupiter_strengths = jupiter_data.get("work_strengths", [])
    jupiter_note = (
        f"Jupiter in {jupiter_sign} expands your professional capacity through "
        f"{jupiter_strengths[0].lower() if jupiter_strengths else 'broadening your perspective'}. "
        f"Opportunities tend to multiply when you lean into these qualities in your work."
    )

    saturn_data     = CAREER_BY_SIGN.get(saturn_sign, {})
    saturn_strengths = saturn_data.get("work_strengths", [])
    saturn_note = (
        f"Saturn in {saturn_sign} asks you to master "
        f"{saturn_strengths[0].lower() if saturn_strengths else 'discipline and structure'} "
        f"as a career foundation. The skills that demand real mastery in this area will be "
        f"your most enduring source of professional authority."
    )

    sun_data     = CAREER_BY_SIGN.get(sun_sign, {})
    sun_strengths = sun_data.get("work_strengths", [])
    sun_note = (
        f"Your Sun in {sun_sign} brings "
        f"{sun_strengths[0].lower() if sun_strengths else 'your core identity'} "
        f"to everything you do. The most fulfilling careers are those that allow this quality "
        f"to be expressed fully, not suppressed."
    )

    synthesis = f"{mc_description}\n\n{sun_note}\n\n{jupiter_note}\n\n{saturn_note}"

    return {
        "mc_sign": mc_sign,
        "professions": professions,
        "work_strengths": work_strengths,
        "synthesis": synthesis,
    }


# ── Romance Section ───────────────────────────────────────────────────────────

ROMANCE_BY_SIGN = {
    "Aries": {
        "love_style": "Bold, direct, and fiercely passionate — you love like you live, at full speed.",
        "what_you_seek": "A partner who can match your energy, keep up with your pace, and handle your directness without flinching. You want someone who challenges you, not someone who simply agrees.",
        "relationship_strengths": ["Passionate and devoted when committed", "Honest and direct about feelings", "Exciting and adventurous partner", "Fiercely protective of loved ones", "Refreshingly uncomplicated in expressing desire"],
        "relationship_challenges": "Impatience and the tendency to move on before fully processing can create a trail of unfinished emotional business. Learning to slow down and stay through the difficult middle of a relationship is the great romantic growth edge.",
        "ideal_partner_qualities": "Independent, confident, physically active, and honest to the point of bluntness. Someone who has their own life and doesn't need you to complete them.",
        "synthesis": "Your Venus sign shapes how you love and what you attract, while your Moon sign reveals what you need to feel emotionally safe in relationship. Together, they describe the full landscape of your romantic world.",
    },
    "Taurus": {
        "love_style": "Sensual, steady, and profoundly loyal — you love through physical presence, devotion, and the patient tending of the relationship over years.",
        "what_you_seek": "Security, consistency, and someone whose love feels like coming home. You want a partner who shows up, who follows through, and who creates with you rather than just existing alongside you.",
        "relationship_strengths": ["Unwavering loyalty and devotion", "Deeply sensual and physically affectionate", "Creates beautiful shared environments", "Financially reliable and stable", "Love that deepens beautifully with time"],
        "relationship_challenges": "Possessiveness and resistance to change can create a slow suffocation of relationships that need room to evolve. Learning to love without clutching is the deep romantic practice.",
        "ideal_partner_qualities": "Stable, warm, aesthetically sensitive, and someone who appreciates the slow art of building something beautiful together. Preferably someone who also loves good food.",
        "synthesis": "Your love is built to last — given to the right person, your devotion becomes one of the rarest and most nourishing forces in another's life. The work is choosing well and then staying present as both of you continue to grow.",
    },
    "Gemini": {
        "love_style": "Playful, intellectually stimulating, and endlessly curious — you fall for minds before bodies and love best when there's always something new to discover in your partner.",
        "what_you_seek": "A partner who can hold a conversation at any hour, who surprises you with new ideas, and who gives you enough space to be the multi-faceted person you are without trying to pin you down to one version.",
        "relationship_strengths": ["Witty, charming, and endlessly entertaining", "Brings lightness and humor to the relationship", "Adaptable and socially brilliant", "Never boring in conversation or in life", "Genuinely curious about their partner"],
        "relationship_challenges": "Emotional depth can feel threatening or inaccessible — the tendency to intellectualize feelings creates distance precisely where closeness is possible. Learning to stay with discomfort rather than talking around it is the romantic growth edge.",
        "ideal_partner_qualities": "Intellectually brilliant, socially fluid, curious about the world, and secure enough not to be threatened by your need for variety and mental stimulation.",
        "synthesis": "Your love is a living conversation — and the most beautiful relationships in your life will be the ones where the conversation never fully ends, because you both keep bringing something new to the table.",
    },
    "Cancer": {
        "love_style": "Deeply tender, instinctively nurturing, and quietly powerful — you create a love so encompassing that those inside it feel like they have finally arrived somewhere safe.",
        "what_you_seek": "Emotional safety, genuine belonging, and a partner who can receive your care without taking it for granted. You want to build a home — not just a structure, but a feeling — with someone who values what that means.",
        "relationship_strengths": ["Deeply empathic and emotionally present", "Nurturing and protective of loved ones", "Creates genuine home and belonging", "Loyal beyond question", "Emotionally intelligent and intuitive"],
        "relationship_challenges": "The crab's shell is the great romantic paradox — you desire intimacy but sometimes armor yourself so thoroughly that it can't find its way in. Learning to stay open when you feel most vulnerable is the work.",
        "ideal_partner_qualities": "Emotionally mature, patient with your tidal moods, genuinely interested in building a life rather than just dating, and capable of the kind of quiet devotion that doesn't need an audience.",
        "synthesis": "Your capacity to love is one of the most profound in the zodiac — you don't love superficially, and the people who receive your love know it changes them. The invitation is to choose partners who are genuinely worthy of that gift.",
    },
    "Leo": {
        "love_style": "Grand, generous, and heart-first — you love with a warmth and enthusiasm that makes your partner feel like the most important person in the world, because in those moments, they are.",
        "what_you_seek": "To be truly seen and adored in return. You give so much that the absence of genuine appreciation feels like abandonment. You want a partner who celebrates you publicly, honors you privately, and matches your passion with their own.",
        "relationship_strengths": ["Romantic and dramatically devoted", "Fiercely loyal once committed", "Creates magic and joy in the relationship", "Generous beyond measure with time, affection, and resources", "Proud of their partner and eager to show it"],
        "relationship_challenges": "The need for attention and appreciation, when unmet, can turn into pride and withdrawal. Learning that love is not a performance — that the deepest intimacy happens offstage — is the great romantic growth of Leo.",
        "ideal_partner_qualities": "Confident, warm, genuinely admiring, and someone who is proud to be seen with you — but who also sees beyond the performance to the tender, uncertain heart underneath.",
        "synthesis": "When you love fully, you light up another person's entire world. The work is ensuring the love you build is as real as the feeling it creates — not a performance, but the full and vulnerable truth of who you are.",
    },
    "Virgo": {
        "love_style": "Quietly devoted, practically expressive, and deeply attentive — you show love through the thousand small ways you make someone's life better without being asked.",
        "what_you_seek": "A partner who notices and appreciates the quality of your care, who meets your high standards for integrity and cleanliness of character, and who can help you relax into love rather than perpetually improving it.",
        "relationship_strengths": ["Deeply attentive to a partner's real needs", "Reliable, trustworthy, and consistent", "Grows better with time and investment", "Thoughtful and considerate in daily life", "Genuine rather than performative in affection"],
        "relationship_challenges": "The inner critic doesn't stay in the office — it follows you into relationships and finds imperfections that, if focused on too heavily, can erode what is genuinely beautiful. Learning to appreciate rather than constantly assess is the romantic practice.",
        "ideal_partner_qualities": "Someone with genuine integrity, who appreciates quality over flashiness, who has their own sense of purpose, and who can handle your directness about what you need — ideally without taking it personally.",
        "synthesis": "You love in the most practical and real of ways — through sustained, daily devotion and the quiet excellence of someone who shows up fully. The person lucky enough to truly receive this will understand what it means to be genuinely cared for.",
    },
    "Libra": {
        "love_style": "Gracious, romantic, and deeply invested in the art of partnership — you approach love as a spiritual collaboration and pour genuine thought and beauty into the relationship.",
        "what_you_seek": "A true equal — someone who brings as much to the relationship as you do, who values harmony and beauty, who communicates with grace, and who wants to build something refined and mutual.",
        "relationship_strengths": ["Exceptionally thoughtful and considerate", "Creates genuine beauty in shared life", "Highly skilled at navigating conflict with grace", "Genuinely interested in their partner's inner world", "Romantic in the truest and most sustained sense"],
        "relationship_challenges": "The fear of conflict and the drive for harmony can create a situation where real feelings are suppressed until they overflow — the very imbalance you were trying to prevent. Learning to speak your needs directly, as an act of love, is the growth edge.",
        "ideal_partner_qualities": "Aesthetically thoughtful, emotionally mature, willing to engage in genuine dialogue, and someone who sees partnership as a life practice rather than a convenient arrangement.",
        "synthesis": "You are capable of creating a love that is genuinely beautiful — where both people are elevated by the connection. The key is ensuring that beauty is built on honesty as well as grace, and that you are as real as you are refined.",
    },
    "Scorpio": {
        "love_style": "Total, transformative, and utterly committed — you don't love halfway, and you have no patience for relationships that live on the surface.",
        "what_you_seek": "A depth of connection that most people never access — a partner who can handle your intensity, match your loyalty, hold your gaze when it gets uncomfortable, and grow through what you create together rather than retreating from it.",
        "relationship_strengths": ["Absolute loyalty and devotion", "Transforms the relationship and their partner for the better", "Intensely passionate and magnetic", "Perceptive about their partner's real nature", "Creates genuine depth of connection"],
        "relationship_challenges": "Jealousy, the testing of loyalty, and the difficulty of releasing control can create a relationship climate that feels like a permanent examination. Learning to trust before being given proof is the great Scorpionic romantic challenge.",
        "ideal_partner_qualities": "Psychologically deep, genuine and consistent, courageous enough to be honest when it's difficult, and secure enough not to be overwhelmed by the full force of what you bring.",
        "synthesis": "The love you are capable of building is among the most powerful transformative forces available to any human being. Guard it carefully, choose well, and allow yourself to be seen — not just to see.",
    },
    "Sagittarius": {
        "love_style": "Expansive, adventurous, and open-hearted — you love with great enthusiasm and are at your best with a partner who doubles as a companion on the endless journey of meaning-making.",
        "what_you_seek": "Freedom within the relationship — room to grow, explore, and become. You want a partner who inspires you philosophically, who is willing to travel (literally or metaphorically), and who doesn't mistake your restlessness for indifference.",
        "relationship_strengths": ["Joyful, enthusiastic, and life-expanding", "Honest to a fault — you will not pretend", "Generous and warm-hearted in love", "Brings adventure and new perspective", "Deeply inspiring to the right partner"],
        "relationship_challenges": "Commitment can feel like a cage before you've examined the lock — the fear of being limited can cause you to bolt before the relationship has found its full depth. Learning to stay through the ordinary middle is where your greatest love story lives.",
        "ideal_partner_qualities": "Independent, intellectually curious, willing to give you space, adventurous in their own right, and someone who understands that your love of freedom is an expression of your philosophy, not a rejection of them.",
        "synthesis": "When you choose to stay — fully and freely — you become one of the most inspiring partners imaginable. The work is discovering that depth and freedom are not opposites, and that the deepest relationships are themselves a form of liberation.",
    },
    "Capricorn": {
        "love_style": "Reserved at first, but irreversibly devoted once committed — your love is the kind that compounds quietly over years and decades, becoming something most people never find.",
        "what_you_seek": "A partner you genuinely respect — someone with substance, integrity, and ambition that complements your own. You are not looking for a feeling; you are looking for a life, and you want to build it with someone worthy.",
        "relationship_strengths": ["Unwavering commitment and loyalty", "Provides genuine security and stability", "Love that deepens and strengthens over time", "Emotionally mature and responsible", "Partner for real life, not just the exciting parts"],
        "relationship_challenges": "The tendency to prioritize work, ambition, or control over emotional availability can create a kind of loneliness within the relationship itself. Learning to be present, warm, and vulnerable — not just reliable — is the romantic growth edge.",
        "ideal_partner_qualities": "Ambitious in their own right, emotionally mature enough to handle your initial reserve, patient with the slow build, and someone who values the substance of what you build together over the drama of what you feel.",
        "synthesis": "Your love is built on rock, not sand — and the person who understands that, and is willing to let it develop at its own pace, will find themselves in a relationship of rare solidity and depth. Allow yourself to also be warm, not just dependable.",
    },
    "Aquarius": {
        "love_style": "Friendly, intellectually intimate, and somewhat paradoxically — both deeply interested in people and occasionally emotionally distant from the one closest to you.",
        "what_you_seek": "A partner who is also your intellectual equal, your best friend, and someone genuinely original enough to keep surprising you. You need room to be yourself — including the parts that don't fit any conventional category.",
        "relationship_strengths": ["Deeply loyal once genuinely committed", "Unique and fascinating to be in relationship with", "Genuinely interested in their partner as a person", "Brings originality and vision to shared life", "Not possessive or controlling"],
        "relationship_challenges": "Emotional distance — the habit of observing rather than feeling — can create a gap in the relationship that closeness cannot fully bridge until you learn to be moved as well as interested. Learning to feel in real time is the great Aquarian romantic practice.",
        "ideal_partner_qualities": "Intellectually stimulating, independent, willing to give you space for your causes and ideas, and someone secure enough not to read your detachment as indifference.",
        "synthesis": "When the walls come down — and they do, with the right person — you are capable of a love that is both deeply authentic and genuinely visionary. The work is letting that person in before they give up waiting.",
    },
    "Pisces": {
        "love_style": "Oceanic, empathic, and soul-level — you fall for the essence of a person, love them in your imagination as much as in reality, and give with a generosity that can be both transcendent and exhausting.",
        "what_you_seek": "A connection that transcends the ordinary — a love that feels fated, spiritually significant, and beautiful in both its joy and its suffering. You want to merge, and you need a partner who will not take advantage of that willingness.",
        "relationship_strengths": ["Compassionate and deeply empathic", "Romantic in the most poetic sense", "Intuitively understands their partner's unspoken needs", "Devoted beyond what most would consider reasonable", "Creates a sense of spiritual depth in the relationship"],
        "relationship_challenges": "The tendency to idealize the beloved — to fall in love with the imagined version rather than the real one — can lead to a painful crash when reality asserts itself. Developing the discernment to choose someone worthy of your devotion, rather than someone who simply needs it, is the essential romantic work.",
        "ideal_partner_qualities": "Emotionally honest, spiritually inclined in some way, capable of genuine devotion, and secure enough in themselves not to confuse your boundlessness for permission to take without giving.",
        "synthesis": "Your capacity for love is one of the most extraordinary in the zodiac — if you direct it wisely. The right person will experience being loved by you as one of the most beautiful things that has ever happened to them. Choose someone who knows that.",
    },
}


def get_romance_reading(placements):
    venus_sign = placements.get("Venus", {}).get("sign")
    moon_sign  = placements.get("Moon",  {}).get("sign")
    asc_sign   = placements.get("Ascendant", {}).get("sign")

    venus_data = ROMANCE_BY_SIGN.get(venus_sign, {})
    moon_data  = ROMANCE_BY_SIGN.get(moon_sign, {})

    # 7th house sign = 6 signs after the ASC sign
    asc_idx = SIGNS.index(asc_sign) if asc_sign in SIGNS else 0
    seventh_house_sign = SIGNS[(asc_idx + 6) % 12]

    moon_note = (
        f"Your Moon in {moon_sign} reveals your emotional needs in relationship: "
        f"{moon_data.get('love_style', '')} "
        f"Emotionally, you feel most secure when {moon_data.get('what_you_seek', 'your needs are met with consistency and care.')}."
    )

    seventh_note = (
        f"Your 7th house — the house of partnership — falls in {seventh_house_sign}, "
        f"meaning you tend to attract and seek out {seventh_house_sign} qualities in partners: "
        f"the traits this sign embodies become both what you are drawn to and what you are learning to integrate within yourself."
    )

    return {
        "venus_sign": venus_sign,
        "moon_sign": moon_sign,
        "seventh_house_sign": seventh_house_sign,
        "love_style": venus_data.get("love_style", ""),
        "what_you_seek": venus_data.get("what_you_seek", ""),
        "relationship_strengths": venus_data.get("relationship_strengths", []),
        "relationship_challenges": venus_data.get("relationship_challenges", ""),
        "ideal_partner": venus_data.get("ideal_partner_qualities", ""),
        "moon_note": moon_note,
        "seventh_note": seventh_note,
        "synthesis": venus_data.get("synthesis", ""),
    }


# ── Transit Interpretations ───────────────────────────────────────────────────

TRANSIT_PLANET_HOUSE = {
    "Sun": {
        1: "The Sun illuminates your 1st house of self — this is a period of personal renewal, heightened visibility, and a natural surge of vitality. Others notice you. Step forward.",
        2: "The Sun activates your resources, self-worth, and income. Review finances, affirm your values, and notice what you truly consider valuable right now.",
        3: "Communication, learning, and local connections are lit up. Ideas flow freely. A good time for writing, networking, and short journeys that open doors.",
        4: "Home, family, and inner foundations are in focus. You may feel drawn inward, toward roots and emotional foundations. A meaningful time for inner work.",
        5: "Creativity, romance, and self-expression receive a solar boost. Play, create, perform, and allow joy to lead you — it knows where to go.",
        6: "Daily health, routines, and work are highlighted. Refine your habits, serve effectively, and attend to the body's signals — they are unusually clear now.",
        7: "Relationships and partnerships take center stage. Key connections are illuminated. A meaningful period for both romantic and professional alliances.",
        8: "Deep transformation, shared resources, and psychological insight are activated. What you have been avoiding may surface — meet it with courage.",
        9: "Expansion, travel, higher learning, and philosophical inquiry are lit. Follow the call toward meaning. A particularly good time to study, travel, or teach.",
        10: "Career, reputation, and public life receive solar energy. Visibility increases — use it deliberately. Decisions made now carry unusual professional weight.",
        11: "Community, friendships, and collective goals are highlighted. Reach out, collaborate, and allow your network to support you and be supported.",
        12: "A time of retreat, rest, and inner integration. Solitude is productive now. What is done quietly behind the scenes carries more power than public action.",
    },
    "Moon": {
        1: "You feel more visible and emotionally responsive than usual. Your moods color your appearance. A time for emotional honesty with yourself.",
        2: "Security and comfort feel especially important. Spend on what nourishes rather than what impresses. Emotional needs and material needs are aligned now.",
        3: "Conversations carry emotional weight. Reach out to siblings, neighbors, or those nearby. Your intuition in communication is unusually accurate.",
        4: "Home pulls at you. Emotional needs around family and belonging are surfacing. Nourish yourself and your inner world — don't push outward now.",
        5: "Play, pleasure, and creative self-expression feel emotionally satisfying. Spend time with children or on creative projects. Let yourself be happy.",
        6: "Attention to the body, diet, and health feels instinctively important. Your emotional state directly affects your physical state — tend to both.",
        7: "Relationships trigger emotional responses — both tender and reactive. A good time for honest emotional conversations with partners.",
        8: "Deep feelings surface. Old grief, desire, or fear may emerge — let them move through. Emotional depth is available now; don't push it away.",
        9: "You feel a pull toward meaning, adventure, and learning. Trust the restlessness — it is pointing toward genuine expansion.",
        10: "Emotional energy goes into career and public responsibilities. Public image feels personal. Don't neglect home life in the service of professional demands.",
        11: "Friends and community feel like family. Social connections are emotionally nourishing now. Reach out — you need your people.",
        12: "Emotions are quieter but deeper. Dreams are vivid. Rest, pray, meditate — the inner world has something important to offer right now.",
    },
    "Mercury": {
        1: "Your thinking is sharp and your communication is unusually direct. A good time to launch ideas, make your voice heard, and begin intellectual projects.",
        2: "Financial decisions benefit from clear thinking. Research investments or income strategies. Talk about money — with yourself or advisors.",
        3: "Mercury in the 3rd is at home — communication is flowing, ideas multiply, and learning happens effortlessly. Write, speak, connect.",
        4: "Family conversations need care. Think through home-related decisions. Childhood patterns may surface for conscious examination.",
        5: "Creative thinking is at its best. Playful, generative, inventive — let your mind play without agenda. Romance may involve significant conversations.",
        6: "Mental energy goes into work systems and health decisions. Analyze, optimize, and communicate clearly with colleagues and care providers.",
        7: "Contracts, agreements, and relationship conversations need thoughtful attention. Be clear — both with yourself and with partners.",
        8: "Research, investigation, and psychological analysis are productive. Your mind penetrates deeper than usual. A good time for difficult but necessary conversations.",
        9: "Philosophical and educational thinking expands. Write, publish, teach, or study. Long-distance communication is favored.",
        10: "Professional communications carry weight. Think carefully before speaking about career matters. Your words build or damage reputation now.",
        11: "Group conversations and collaborative thinking are productive. Your ideas resonate with communities and networks. Share them widely.",
        12: "Thinking is more private and introspective. Journaling, meditation, and research done in solitude are rewarding. Don't try to force clarity — let it arrive.",
    },
    "Venus": {
        1: "You radiate charm, beauty, and social magnetism. Attraction increases — both given and received. A favorable time for first impressions and new connections.",
        2: "Financial and material pleasures are highlighted. Treat yourself thoughtfully. Your sense of worth is being evaluated — invest in what genuinely matters.",
        3: "Social connections and local pleasures bring joy. Beauty in communication — words flow with grace. A good time to reach out to those you've neglected.",
        4: "Home becomes a place of beauty and comfort. Family relationships warm. Invest in your living environment and in the people who make it feel like home.",
        5: "Romance, creativity, and pleasure are at their peak. Flirt, create, play, and let yourself fall a little — in love, in art, in joy.",
        6: "Harmony in daily work and health routines is available. Collaboration improves. Beauty in small things becomes a source of genuine wellbeing.",
        7: "Partnerships flourish. Existing relationships warm and deepen. New connections have unusual romantic or professional potential. Meet people.",
        8: "Intimate relationships are intensified. Shared resources, physical closeness, and emotional depth are all available — if you are willing to go there.",
        9: "Beauty in ideas, travel, and cultural exchange. An aesthetically inspiring period. Love may arrive from afar — geographically or philosophically.",
        10: "Charm and grace serve your professional reputation. Social connections further career goals. A good time for networking, presentations, and public-facing work.",
        11: "Social life expands joyfully. Friendships may deepen into romance. Group activities and communities bring genuine pleasure and belonging.",
        12: "Love in secret or in solitude. Longing rises. A time for inner romantic work — examining what you truly want and healing what has been disappointed.",
    },
    "Mars": {
        1: "Energy, drive, and physical vitality surge. You are ready to act — make sure the direction is worth the intensity. Impulsiveness needs conscious direction.",
        2: "Drive goes toward earning, building financial security, and asserting your values. A good time to pursue income increases and defend what you have worked for.",
        3: "Mental energy is sharp and direct — possibly too sharp in conversation. Think, write, drive, and communicate with deliberate purpose.",
        4: "Energy in the home can mean productive renovation or family friction. Channel Mars constructively here — domestic projects thrive, but tempers flare more easily.",
        5: "Creative energy is at its peak. Pursue what excites you — art, romance, physical pleasure, competitive play. This is productive passion.",
        6: "Work productivity increases dramatically. Health routines gain intensity. Push forward on practical goals, but monitor for burnout or overexertion.",
        7: "Relationship dynamics become more active — and potentially more tense. Assert your needs while remaining open to your partner's. Negotiate, don't dictate.",
        8: "Drive toward transformation, depth, and resource management intensifies. Sexual energy rises. A powerful time to pursue what you want — with awareness.",
        9: "Energy goes toward learning, travel, philosophy, and the pursuit of meaning. A good time for competitive academic or ideological endeavors.",
        10: "Career ambition peaks. Push forward on professional goals — this is not a time to wait. Visibility increases; use it strategically.",
        11: "Group activities and collaborative projects benefit from your drive. Lead within communities, but avoid imposing your agenda on collective goals.",
        12: "Energy turns inward — frustration may arise if you try to push outward without result. Rest, retreat, and allow the inner fire to clarify its direction.",
    },
    "Jupiter": {
        1: "A period of expansion, optimism, and personal growth. You feel larger than your current circumstances. Opportunities for self-improvement abound — embrace them.",
        2: "Financial expansion and increased abundance are likely. This is one of the most favorable transit periods for income growth. Trust your capacity to attract.",
        3: "Learning, communication, and intellectual expansion flourish. Courses, books, conversations — fill your mind with what excites and enlarges your worldview.",
        4: "Home, family, and inner foundations benefit from expansion. Consider improving your living situation, deepening family bonds, or healing old roots.",
        5: "Creative output increases and romantic opportunity expands. This is a particularly joyful Jupiter transit — lean into whatever brings you delight.",
        6: "Health improves and daily work becomes more rewarding. Service brings satisfaction. An excellent time to improve routines and upgrade working conditions.",
        7: "Partnerships and alliances expand. Existing relationships benefit from generosity and growth. New connections — romantic or professional — carry unusual promise.",
        8: "Transformation, shared resources, and psychological expansion. Financial support may arrive through others. Inner breakthroughs are available if you seek them.",
        9: "Jupiter in the 9th is at home — one of the most auspicious transit periods available. Travel, study, publish, teach, and expand your worldview. Say yes.",
        10: "Career reaches a meaningful peak. Recognition, promotion, and professional opportunity are favored. Position yourself where the opportunity can find you.",
        11: "Community, friendships, and collective endeavors expand joyfully. Collective goals advance. Your network becomes a genuine source of abundance.",
        12: "Spiritual growth, inner wisdom, and compassionate service expand quietly. What is released or surrendered during this transit creates enormous inner room.",
    },
    "Saturn": {
        1: "A period of recalibration, discipline, and self-examination. You are being asked to show up more authentically and to carry your responsibilities with genuine maturity.",
        2: "Financial structures are being tested. Spend carefully, avoid debt, and focus on building sustainable income rather than quick gains. Security requires real work now.",
        3: "Communication requires precision and care. Serious conversations are productive. Commit to learning something deeply rather than skimming many things.",
        4: "Home, family, and inner foundations require attention and sometimes significant restructuring. Facing what was avoided here creates genuine stability.",
        5: "Creative expression requires discipline to manifest. Romance may feel heavy or restricted. The playfulness of this house needs Saturn's structure to become real art.",
        6: "Health and work routines require accountability. Build serious daily disciplines — they will compound into significant wellbeing over time.",
        7: "Relationships are tested for genuine compatibility and mutual accountability. Partnership becomes real work — but the ones that survive emerge with genuine depth.",
        8: "Transformation, shared resources, and deep psychological work require sustained effort. Financial agreements need careful attention. Face what you have been avoiding.",
        9: "Beliefs, philosophy, and worldview are being examined with rigorous honesty. Travel may be restricted but inner expansion through serious study is possible.",
        10: "Career authority and public responsibility increase significantly. Saturn here either rewards years of genuine effort or demands a reckoning for shortcuts taken.",
        11: "Community and group involvement require realistic assessment. Long-term friendships may be tested. Networks that survive become your most durable support.",
        12: "Saturn in the 12th is one of the most inward and sometimes difficult placements — old karma is being processed. What is released here creates freedom that follows.",
    },
    "Rahu": {
        1: "Rahu activates your 1st house — a period of intensified ambition, increased visibility, and sometimes restless craving for more. Who you are becoming is in accelerated development.",
        2: "Material desire intensifies. Wealth accumulation is possible, but the craving can exceed the wisdom. Examine what you truly need versus what you simply want.",
        3: "Communication, media, and networking become avenues for unusual ambition. Ideas spread rapidly. A period of accelerated intellectual growth and social reach.",
        4: "Home and family life are in flux. The familiar becomes strangely unfamiliar. A period of change in domestic life that, navigated consciously, creates genuine new roots.",
        5: "Creative ambition and romantic desire intensify. Children or creative projects may occupy unusual importance. A period of passionate investment in what you love.",
        6: "Intensity in work, service, and health. Unusual challenges in daily life push toward growth. The work environment may feel destabilizing — use it to get real.",
        7: "Relationships become a site of unusual intensity and sometimes obsession. Partnerships that arrive now carry karmic weight. Choose partnerships with clear eyes.",
        8: "Deep psychological and financial intensity. Transformation is accelerated. What is dug up now cannot be ignored — meet it with genuine courage and curiosity.",
        9: "An unusual hunger for meaning, travel, and higher knowledge. Spiritual seeking intensifies — but examine whether you are seeking truth or simply escaping.",
        10: "Career ambition surges. Rapid rise in public visibility. A period of significant professional development — just ensure the foundation is solid enough for the height.",
        11: "Intense engagement with groups, networks, and collective causes. Social ambition rises. Unusual friends and connections arrive — not all of them will stay.",
        12: "A complex transit that can bring both intensified spirituality and increased confusion. Rest, retreat, and pay attention to dreams — the unconscious is unusually active.",
    },
    "Ketu": {
        1: "Ketu in the 1st creates a sense of identity dissolution — who you think you are is being released. A period of unusual detachment from the ego that can feel disorienting but is deeply liberating.",
        2: "Detachment from material security and possessions. Financial concerns either resolve unexpectedly or cease to feel as urgent. Inner wealth becomes more real than outer.",
        3: "Detachment from conventional thinking and communication. Silence carries more meaning than words right now. Deep insight arrives through stillness, not conversation.",
        4: "A sense of detachment from home, family, or roots. Old patterns of belonging are releasing. A good time for ancestral healing and inner excavation.",
        5: "Detachment from creative output and romantic attachment. Past romantic karma may surface for release. Creative work becomes more meditative than expressive.",
        6: "Old health patterns and work habits are releasing. Service becomes less about recognition and more about genuine offering. Simplify, streamline, and let go.",
        7: "Relationship karma surfaces. Past relationship patterns — inherited or self-created — are releasing. A period of genuine liberation from unhealthy relational patterns.",
        8: "Deep karmic material is surfacing for resolution. Psychological and financial entanglements from the past are being cleared. Surrender is more productive than control.",
        9: "Detachment from established beliefs and philosophical systems. Old religious or philosophical frameworks may feel hollow. What remains is the direct experience beneath all doctrine.",
        10: "Detachment from status, recognition, and conventional career goals. What you have been working toward may feel less important. What genuinely matters becomes clearer.",
        11: "Detachment from social networks and group affiliations. Old friendships may fade as new directions emerge. A more solitary but more authentic social landscape develops.",
        12: "Ketu in the 12th is deeply spiritual — a period of accelerated inner development, unusual psychic sensitivity, and the dissolution of old karmic debris. Meditate.",
    },
}


def get_transit_interpretation(planet, house):
    planet_data = TRANSIT_PLANET_HOUSE.get(planet, {})
    return planet_data.get(house, f"{planet} transiting your {house}th house activates that area of life with the qualities of {planet}'s energy.")


# ─── Dasha Interpretations ─────────────────────────────────────────────────────

DASHA_INTERPRETATIONS = {
    "Ketu": (
        "Ketu Maha Dasha brings a powerful period of spiritual deepening, detachment, and inner reckoning. "
        "External ambitions tend to lose their grip as life turns you inward — toward meditation, solitude, "
        "and the dissolution of old identities. Past-life karma surfaces for release, and what you thought "
        "you wanted may reveal itself as borrowed desire. This is a period of profound letting go and "
        "mysterious gifts: psychic sensitivity, artistic depth, and liberation from the ego's demands."
    ),
    "Venus": (
        "Venus Maha Dasha is one of the most benefic and abundant periods in the Vimshottari cycle, "
        "spanning 20 years of creativity, beauty, love, and material flourishing. Relationships deepen "
        "and new ones blossom. Artistic talent expands. Financial opportunities arise through beauty, "
        "luxury, and partnership. The shadow side is indulgence and comfort-seeking — the invitation "
        "is to enjoy the world fully while cultivating gratitude and discernment."
    ),
    "Sun": (
        "Sun Maha Dasha is a 6-year period of identity, leadership, and self-expression. The authentic "
        "self steps forward. Career recognition and public visibility often increase. Relationships with "
        "authority figures — fathers, bosses, governments — become significant. This is a time to step "
        "into your dharma with courage, though pride and ego-inflation must be consciously watched."
    ),
    "Moon": (
        "Moon Maha Dasha spans 10 years of heightened emotional sensitivity, nurturing, and intuitive "
        "expansion. Home, family, and roots take center stage. The inner life becomes richer and more "
        "vivid. Creative and psychic abilities often awaken. Emotional patterns from early life surface "
        "for healing. The invitation is to cultivate emotional intelligence and let feeling guide you "
        "toward your truest belonging."
    ),
    "Mars": (
        "Mars Maha Dasha is a 7-year period of drive, courage, and fierce forward movement. Energy "
        "surges — physically, professionally, and sexually. Ambition crystallizes and action becomes "
        "decisive. Conflicts may arise as you assert your will and claim your ground. The higher "
        "expression of Mars here is disciplined effort, athletic mastery, and protective strength. "
        "The shadow is aggression, impatience, and recklessness."
    ),
    "Rahu": (
        "Rahu Maha Dasha lasts 18 years and governs ambition, obsession, foreign influence, and the "
        "pursuit of that which is novel, unconventional, or taboo. Worldly desires amplify. Career "
        "breakthroughs through technology, media, or foreign cultures are common. The sense of self "
        "may feel unstable or inflated. This period rewards those who pursue their desires with "
        "awareness — transformation comes through engagement with the material world and its illusions."
    ),
    "Jupiter": (
        "Jupiter Maha Dasha spans 16 years of wisdom, expansion, grace, and dharmic growth. Teachers, "
        "mentors, and spiritual communities enter your life. Higher education, philosophy, law, and "
        "healing arts are favored. Financial and social expansion often follows. This is a period of "
        "true blessing when you align your actions with truth and generosity. Complacency and "
        "over-optimism are the pitfalls to watch."
    ),
    "Saturn": (
        "Saturn Maha Dasha lasts 19 years of structure, discipline, and karmic accountability. Life "
        "slows down and demands patience, effort, and maturity. Shortcuts dissolve; only what is "
        "genuinely solid survives. Career advancement through consistent work is possible, though "
        "delays are common. Health, longevity, and ancestral patterns come into focus. The gift of "
        "this dasha — earned slowly — is mastery, integrity, and enduring achievement."
    ),
    "Mercury": (
        "Mercury Maha Dasha spans 17 years of communication, intellect, commerce, and learning. "
        "Writing, speaking, teaching, trading, and networking all flourish. The mind is sharp and "
        "adaptable. Education and technical skills deepen. Sibling relationships, short journeys, "
        "and media become important. Mercury rewards those who communicate clearly and learn "
        "continuously — the shadow is scattered thinking and verbal cunning without wisdom."
    ),
}

ANTAR_DASHA_NOTES = {
    "Ketu":    "Spiritual withdrawal, past-life themes, and sudden insights characterize this sub-period.",
    "Venus":   "Love, creativity, and material pleasures are highlighted in this sub-period.",
    "Sun":     "Authority, visibility, and self-assertion are emphasized in this sub-period.",
    "Moon":    "Emotional depth, intuition, and home/family themes dominate this sub-period.",
    "Mars":    "Drive, conflict, and decisive action define this sub-period.",
    "Rahu":    "Ambition, foreign influence, and unexpected changes mark this sub-period.",
    "Jupiter": "Wisdom, opportunity, and spiritual grace bless this sub-period.",
    "Saturn":  "Discipline, delays, and karmic lessons characterize this sub-period.",
    "Mercury": "Communication, learning, and business activity flourish in this sub-period.",
}


def get_dasha_interpretation(lord):
    return DASHA_INTERPRETATIONS.get(lord, f"{lord} Maha Dasha activates the themes of {lord} in your life.")


# ─── Fixed Star Interpretations ────────────────────────────────────────────────

FIXED_STAR_PLANET_MEANINGS = {
    "Algol": {
        "default": "Algol (the Demon Star, β Persei) conjunct this planet intensifies its power to the extreme — capable of profound destruction and equally profound transformation. The energy is raw, primal, and karmic.",
        "Sun": "The Sun conjunct Algol bestows immense personal power and magnetism, but often brings a defining trial — a fall from which one must rise transformed. Resilience and shadow-integration are essential.",
        "Moon": "The Moon conjunct Algol heightens emotional intensity and psychic ability, but may bring ancestral trauma, obsession, or sudden reversals through emotional entanglement. Great depth lies here.",
        "Mercury": "Mercury conjunct Algol sharpens the mind to a cutting edge — brilliant, probing, and occasionally ruthless. Investigative, forensic, or occult fields are strongly activated.",
        "Venus": "Venus conjunct Algol brings magnetic, all-consuming attraction. Love affairs may be fated and intense. Beauty is tied to power. Financial extremes — great gain or loss — are possible.",
        "Mars": "Mars conjunct Algol is the warrior at full force — daring, combative, and capable of extraordinary feats. Military, surgical, or extreme sports careers are amplified.",
        "Jupiter": "Jupiter conjunct Algol can bring great wealth or spiritual authority — but tests the integrity with which that power is used. Transformation through philosophy or religion is possible.",
        "Saturn": "Saturn conjunct Algol brings intense karmic trials, often through loss or restriction. Mastery is achieved only after confronting the darkest material in one's life.",
        "Rahu": "Rahu conjunct Algol intensifies worldly obsession and karmic entanglement. Extraordinary ambition — and the need for conscious use of power.",
        "Ketu": "Ketu conjunct Algol suggests deep past-life trauma and the need for spiritual liberation from destructive karmic cycles.",
        "Ascendant": "The rising star Algol marks a life of intensity, extremes, and transformation. Great personal power is available — and must be used with care.",
    },
    "Aldebaran": {
        "default": "Aldebaran (Eye of the Bull, α Tauri) is one of the four Royal Stars of Persia. It bestows honor, authority, courage, and worldly success — but demands integrity.",
        "Sun": "The Sun conjunct Aldebaran marks a natural leader, often rising to prominence in their field. Success is possible on a grand scale when backed by integrity.",
        "Moon": "The Moon conjunct Aldebaran brings emotional courage and public recognition. The inner life is noble and strong. Public roles — especially caregiving or leadership — are favored.",
        "Mercury": "Mercury conjunct Aldebaran gives a commanding voice and sharp intellect. Public speaking, law, and leadership communication are highlighted.",
        "Venus": "Venus conjunct Aldebaran attracts admiration and enduring partnerships. Artistic work achieves recognition. Wealth through beauty or social influence is possible.",
        "Mars": "Mars conjunct Aldebaran is one of the most powerful warrior placements. Courage, decisiveness, and military or competitive honors are indicated.",
        "Jupiter": "Jupiter conjunct Aldebaran brings great wisdom, spiritual authority, and often worldly honor or wealth. A truly auspicious combination.",
        "Saturn": "Saturn conjunct Aldebaran indicates authority earned through perseverance and integrity. Success arrives late but endures.",
        "default": "Aldebaran bestows worldly honor, authority, and success when integrity is maintained.",
    },
    "Regulus": {
        "default": "Regulus (α Leonis, the Heart of the Lion) is the star of royalty, ambition, and sudden elevation — followed by a fall if revenge or ego corruption enters.",
        "Sun": "The Sun conjunct Regulus is the mark of a king or leader — magnetic, powerful, and destined for prominence. The warning: avoid revenge and maintain nobility.",
        "Moon": "The Moon conjunct Regulus brings public renown and emotional leadership. A powerful placement for those in the public eye.",
        "Mercury": "Mercury conjunct Regulus gives sharp, commanding intelligence. Excellent for politics, law, and any field requiring intellectual authority.",
        "Venus": "Venus conjunct Regulus bestows great social charm, beauty, and the potential for fame through artistic or relational gifts.",
        "Mars": "Mars conjunct Regulus creates a natural warrior with military or competitive honors — provided the ego is kept in check.",
        "Jupiter": "Jupiter conjunct Regulus is deeply auspicious: wisdom, abundance, and spiritual leadership at the highest levels.",
        "Saturn": "Saturn conjunct Regulus brings power through patience and discipline — but warns against using authority for revenge.",
        "default": "Regulus activates themes of royalty, ambition, and the responsibility of power.",
    },
    "Spica": {
        "default": "Spica (α Virginis) is the most fortunate star in the sky — associated with gifts, brilliance, spiritual blessings, and success in arts and sciences.",
        "Sun": "The Sun conjunct Spica marks a gifted individual — creative, intelligent, and often blessed with unexpected opportunities and recognition.",
        "Moon": "The Moon conjunct Spica is deeply auspicious: emotional grace, artistic sensitivity, and a blessed personal life are indicated.",
        "Mercury": "Mercury conjunct Spica is one of the finest intellectual placements — exceptional writing, research, or scientific talent with real-world impact.",
        "Venus": "Venus conjunct Spica is a gift from the cosmos: beauty, artistic mastery, and love that feels fated and fulfilling.",
        "Mars": "Mars conjunct Spica brings inspired action and the ability to achieve great things with grace rather than force.",
        "Jupiter": "Jupiter conjunct Spica is among the most benefic combinations in fixed star astrology: wisdom, abundance, spiritual grace, and enduring success.",
        "Saturn": "Saturn conjunct Spica can bring success through dedicated craft. Discipline here creates lasting, beautiful work.",
        "default": "Spica bestows gifts, grace, and the blessings of Venus and Mercury combined.",
    },
    "Antares": {
        "default": "Antares (α Scorpii, Heart of the Scorpion) is one of the four Royal Stars — the rival of Mars. Intensity, passion, obsession, and the warrior archetype are its signatures.",
        "Sun": "The Sun conjunct Antares marks a passionate, driven individual willing to sacrifice everything for their cause. Power and danger exist in equal measure.",
        "Moon": "The Moon conjunct Antares intensifies emotional life to extremes. Deep passion, psychic sensitivity, and the need to confront shadow are all present.",
        "Mercury": "Mercury conjunct Antares gives a penetrating, strategic mind — excellent for research, investigation, and any field requiring ruthless clarity.",
        "Venus": "Venus conjunct Antares brings intense, consuming love and a magnetism that borders on obsessive. The passion here is life-changing.",
        "Mars": "Mars conjunct Antares is a warrior's warrior — formidable, unyielding, and capable of remarkable feats of courage and endurance.",
        "Jupiter": "Jupiter conjunct Antares brings philosophical intensity and the capacity for transformative spiritual teaching.",
        "Saturn": "Saturn conjunct Antares creates a powerful but demanding life path — intense discipline forging rare strength.",
        "default": "Antares activates passion, intensity, and the warrior's willingness to go all in.",
    },
    "Vega": {
        "default": "Vega (α Lyrae) carries the gifts of charisma, artistic brilliance, and natural magnetism — the star of the inspired musician and visionary.",
        "Sun": "The Sun conjunct Vega marks a charismatic individual with natural gifts in music, art, or leadership. Others are naturally drawn to them.",
        "Moon": "The Moon conjunct Vega brings lyrical emotional sensitivity and artistic or musical talent. The soul has a natural beauty.",
        "Mercury": "Mercury conjunct Vega gives poetic eloquence and a gift for languages, music, or inspired communication.",
        "Venus": "Venus conjunct Vega is one of the finest placements for artistic excellence — beauty, music, and love at their most luminous.",
        "Mars": "Mars conjunct Vega channels drive into creative and artistic endeavors. The warrior here creates rather than destroys.",
        "Jupiter": "Jupiter conjunct Vega brings inspired teaching, spiritual artistry, and the gift of uplifting others through wisdom.",
        "Saturn": "Saturn conjunct Vega refines artistic gifts through discipline — mastery achieved through patient dedication to craft.",
        "default": "Vega activates charisma, artistic vision, and the magnetic quality of inspired presence.",
    },
    "Fomalhaut": {
        "default": "Fomalhaut (α Piscis Austrini) is the Autumn Royal Star — the star of idealism, vision, and spiritual aspiration. Dreams here are vivid and potentially prophetic.",
        "Sun": "The Sun conjunct Fomalhaut marks a visionary individual — idealistic, spiritually oriented, and capable of inspiring others with a dream of a better world.",
        "Moon": "The Moon conjunct Fomalhaut heightens intuition and spiritual sensitivity. Dreams and visions carry genuine guidance.",
        "Mercury": "Mercury conjunct Fomalhaut brings prophetic and visionary thinking. Idealism in communication — poetry, spiritual writing, or inspired teaching.",
        "Venus": "Venus conjunct Fomalhaut brings idealized love and spiritual beauty. Relationships feel fated and otherworldly.",
        "Mars": "Mars conjunct Fomalhaut channels drive toward idealistic causes — the crusader who fights for a vision of the sacred.",
        "Jupiter": "Jupiter conjunct Fomalhaut is deeply spiritual and visionary — wisdom that transcends convention.",
        "Saturn": "Saturn conjunct Fomalhaut grounds the visionary in discipline. Spiritual ideals are made practical and lasting.",
        "default": "Fomalhaut activates spiritual vision, idealism, and the pursuit of sacred dreams.",
    },
    "Achernar": {
        "default": "Achernar (α Eridani, End of the River) represents the completion of a great journey — purification, spiritual refinement, and success after deep trials.",
        "Sun": "The Sun conjunct Achernar marks someone whose life path involves great purification — a hero's journey that ultimately leads to spiritual clarity and recognition.",
        "Moon": "The Moon conjunct Achernar brings emotional journeys through depth and purification. Sensitivity to endings and karmic completion.",
        "Mercury": "Mercury conjunct Achernar brings insight into endings, deep psychological patterns, and the wisdom that comes from going all the way through.",
        "Venus": "Venus conjunct Achernar brings love through profound experiences — relationships that purify and transform.",
        "Mars": "Mars conjunct Achernar drives through obstacles with the force of a river — unstoppable determination leading to eventual triumph.",
        "Jupiter": "Jupiter conjunct Achernar brings wisdom and grace after trials — the sage who has crossed the river and returned to teach.",
        "Saturn": "Saturn conjunct Achernar speaks of long karmic journeys toward mastery — profound achievement at the end of great effort.",
        "default": "Achernar activates purification, completion, and the wisdom earned through deep trials.",
    },
}


def get_fixed_star_interpretation(star, planet="default"):
    star_data = FIXED_STAR_PLANET_MEANINGS.get(star, {})
    return star_data.get(planet) or star_data.get("default", f"{planet} conjunct {star} intensifies the themes of both in your chart.")


# ─── Daily Sidereal Horoscopes ─────────────────────────────────────────────────

# 12 signs × 5 themed messages (rotated by day of year mod 5)
DAILY_HOROSCOPE_BY_SIGN = {
    "Aries": [
        "The sidereal Sun moves through the stars that once marked the Pleiades and Aldebaran — your fire is ancient and directional today. Act on what you've been hesitating about. Courage precedes clarity.",
        "Mars, your ruling planet, charges forward in the sky. Channel this energy into physical movement and decisive action rather than reactive conflict. Your strength is a tool, not a weapon.",
        "Relationships ask for your honest voice today. Sidereal Aries carries the energy of the original warrior — one who protects by speaking truth, not by winning arguments.",
        "Career ambitions receive planetary support. Your natural drive positions you ahead of those who are still deliberating. Trust your instincts and make the first move.",
        "A moment of stillness this morning will amplify the rest of your day. Even Aries benefits from the breath before the leap. Set your intention before you act.",
    ],
    "Taurus": [
        "The Moon's passage through your sky today activates your senses and your appetite for beauty. Engage with something physical and beautiful — food, nature, music, touch.",
        "Venus favors your financial affairs. A practical decision made today about money, property, or resources has longer staying power than it might appear. Trust your embodied instincts.",
        "Your relationships need presence more than grand gestures today. Sidereal Taurus is the builder — show up consistently and the foundation deepens.",
        "Creative work flourishes when you slow down enough to feel it. Your hands and body are intelligent today. Let them lead.",
        "Stability is not stagnation — it is the ground from which everything grows. Honor what you have built before reaching for more.",
    ],
    "Gemini": [
        "Mercury activates your mental clarity today. Write, speak, or have the conversation you have been circling around. Words carry unusual precision right now.",
        "The dual nature of sidereal Gemini is a gift — you see multiple perspectives simultaneously. Use this to bridge, not to scatter. Find the thread that connects.",
        "Short journeys, new contacts, and unexpected information all carry significance today. Stay curious and slightly loose — the best insight may arrive sideways.",
        "Your relationship with a sibling, close friend, or collaborator is highlighted. A real conversation — even a difficult one — strengthens the bond.",
        "The mind wants to spin today. Give it an anchor: one task, one question, one creative problem to solve. Focused Gemini energy is extraordinarily productive.",
    ],
    "Cancer": [
        "The Moon, your ruling luminary, speaks directly to your intuition today. Your first feeling about a person or situation is more accurate than your second thought.",
        "Home and family are calling for your attention. Something in your domestic sphere — a conversation, a repair, a ritual — will ground and restore you.",
        "Your sensitivity today is not a weakness — it is antenna. What are you picking up from the people around you? Trust the data your body is collecting.",
        "Sidereal Cancer carries the energy of the nurturing warrior — fierce in protection, soft in presence. Both qualities are available to you today.",
        "Creative and emotional expression go together now. Art, cooking, journaling, or any act of making something nourishing will elevate your day.",
    ],
    "Leo": [
        "The Sun's current sidereal position illuminates your natural radiance. Step forward today — a hesitant Leo wastes the day. You were built to shine, not to dim yourself in deference.",
        "Your creative instincts are sharp and reliable today. A project, a performance, or a bold personal statement will land with impact.",
        "Relationships benefit from your warmth and generosity of spirit. Sidereal Leo at its finest gives without needing recognition — and paradoxically receives the most.",
        "Career and public life receive solar emphasis. Your natural authority is visible. Use it with grace and genuine heart.",
        "Children, playfulness, and creative joy are today's medicine. Whatever makes you laugh and feel alive — pursue that. Even briefly.",
    ],
    "Virgo": [
        "Mercury brings analytical precision today. A problem that has felt complex becomes solvable when you break it into its component parts. Start with what you can actually control.",
        "Your body is communicating today. Pay attention to small signals — sleep, digestion, tension. Sidereal Virgo rules the sacred-ordinary relationship between soul and flesh.",
        "Service is your love language. Find one concrete way to be useful to someone today — not from self-erasure, but from the quiet satisfaction of competence offered freely.",
        "Details matter today in ways they often don't. Read the fine print, double-check the number, ask the clarifying question. Your discernment catches what others miss.",
        "Discernment and criticism are both Mercury's tools — choose discernment. What in your life is genuinely working well? Honor it before fixing what isn't.",
    ],
    "Libra": [
        "Venus highlights your relational intelligence today. The balance you are seeking in a relationship or partnership comes through honest conversation, not accommodation.",
        "Beauty, aesthetics, and harmony hold real meaning today. Sidereal Libra knows that creating a beautiful environment is not vanity — it is a form of spiritual practice.",
        "A decision that has been sitting in ambiguity is ready to be made. You have gathered enough information. Trust your scales — they know when balance has been reached.",
        "Justice and fairness matter to you at a deep level today. If something feels unjust, say so with grace. Your voice for balance is needed.",
        "Social connections carry significance. A casual encounter today may become meaningful later. Bring your full, present self to interactions.",
    ],
    "Scorpio": [
        "Mars and Ketu co-rule your sidereal sign — today brings depth, intensity, and the kind of perception that sees through surfaces. Use it wisely.",
        "Transformation is available today. Something that has been stuck — a feeling, a pattern, a circumstance — is ready to shift if you're willing to look at it directly.",
        "Intimacy — emotional, creative, or physical — is where your power lives today. Don't be afraid of depth. You were built for it.",
        "A financial or resource matter benefits from your investigative instincts. Research, uncover, follow the trail. Your detective mind finds what others overlook.",
        "Release something you have been holding onto. Sidereal Scorpio is the sign of composting — the dead matter becomes the most fertile soil. Let go.",
    ],
    "Sagittarius": [
        "Jupiter expands your vision today. Think bigger than the constraints currently before you. The question is not what is possible right now — it is what direction points toward truth.",
        "Teaching, learning, or philosophical inquiry carries unusual resonance today. Read something that challenges your current worldview. Sidereal Sagittarius grows through honest inquiry.",
        "A journey — physical or philosophical — is calling. Even a short trip or a new idea explored deeply can realign your direction.",
        "Your natural optimism is a genuine spiritual force today, not mere positivity. Share it generously. People around you are lifted by your vision.",
        "Ethics and integrity are Sagittarius's north star. A decision requiring moral clarity becomes easier when you ask: what is genuinely right, rather than what is convenient.",
    ],
    "Capricorn": [
        "Saturn, your ruling planet, rewards patience and consistent effort today. The slow work is the real work. What you build carefully now outlasts what is rushed.",
        "Career ambitions are activated. Your natural authority and competence are visible to the right people today. Show up prepared and let your track record speak.",
        "The relationship between discipline and freedom is your lifelong teacher. Today, genuine freedom comes through meeting one commitment with full presence.",
        "Your reputation is built one choice at a time. A moment of integrity today — even a small one — compounds into something larger over time.",
        "Your ancestors and lineage are present in some way today. Honor what was built before you, even as you build something new.",
    ],
    "Aquarius": [
        "Saturn and Rahu co-rule your sidereal sign — today brings both grounded structure and visionary innovation. You can work within systems and reimagine them at the same time.",
        "Community, collective work, and social contribution are highlighted. Your individual gifts matter most when offered to something larger than yourself.",
        "An unconventional idea you have been holding deserves to be tested. Sidereal Aquarius is the sign of the visionary who experiments rather than merely theorizes.",
        "Friendship and chosen family carry deep meaning today. A conversation with a trusted friend can reorient something that has been unclear.",
        "Technology, networks, and new systems are in your wheelhouse today. Apply your innovative thinking to a problem that has been resisting conventional solutions.",
    ],
    "Pisces": [
        "Jupiter and Ketu co-rule your sidereal sign — today is saturated with intuition, spiritual sensitivity, and the kind of perception that comes from deep listening.",
        "Art, music, meditation, or any practice that dissolves ordinary boundaries is profoundly nourishing today. You need beauty the way others need oxygen.",
        "Your compassion is a genuine superpower today. Someone in your circle needs to be seen and heard. You have the gift of witnessing — use it.",
        "Dreams and intuitive flashes carry unusual clarity. Keep a notebook close. What arrives in sleep or stillness is worth recording.",
        "The boundary between your own feelings and those of others can blur today. Ground yourself before engaging with emotionally heavy situations. Your sensitivity is real — protect it.",
    ],
}


def get_daily_horoscope(sign, day_seed=None):
    """Return today's horoscope for a given sidereal sign."""
    import datetime as dt
    if day_seed is None:
        day_seed = dt.date.today().timetuple().tm_yday
    messages = DAILY_HOROSCOPE_BY_SIGN.get(sign, [])
    if not messages:
        return f"The stars hold deep wisdom for {sign} today. Trust your intuition and remain open to what the cosmic currents bring."
    return messages[day_seed % len(messages)]


# ─── Nakshatra Rituals, Affirmations & Journal Prompts ─────────────────────────

NAKSHATRA_RITUALS = {
    "Ashwini": {
        "affirmation": "I move forward with speed and trust. Healing begins with the first step.",
        "ritual": "Begin something new today — even something small. Light a candle at sunrise and set a single intention for rapid movement.",
        "journal_prompt": "Where in my life am I waiting when I could be moving? What would I attempt if I trusted my instincts completely?",
    },
    "Bharani": {
        "affirmation": "I carry what must be carried with strength and surrender.",
        "ritual": "Honor the cycles of creation and release. Write down something you are ready to release, then burn or bury the paper.",
        "journal_prompt": "What am I gestating? What creation — physical, emotional, or spiritual — is ready to move from seed to form?",
    },
    "Krittika": {
        "affirmation": "I cut away what is false and burn bright with what is real.",
        "ritual": "Light a fire or candle. Sit with its heat and clarity. Let it reveal what needs purification in your life today.",
        "journal_prompt": "What in my life needs a clean, clear cut? Where am I tolerating something impure that diminishes me?",
    },
    "Rohini": {
        "affirmation": "I am fertile ground. What I love, I grow.",
        "ritual": "Tend to something living — a plant, a garden, a creature. Touch the earth. Cook a nourishing meal with full presence.",
        "journal_prompt": "What am I cultivating? Where is beauty and abundance already growing in my life that I have been overlooking?",
    },
    "Mrigashira": {
        "affirmation": "I seek with an open heart. The searching is sacred.",
        "ritual": "Go for a walk with no destination in mind. Let curiosity guide your steps. Notice what draws your attention.",
        "journal_prompt": "What am I searching for? Is the seeking itself the teaching — or have I already found what I seek and not recognized it?",
    },
    "Ardra": {
        "affirmation": "I am the storm and the calm after. I am strong enough for both.",
        "ritual": "Spend time in rain or near water today. Let yourself feel the full force of an emotion without acting on it. Witness it pass.",
        "journal_prompt": "What storm is passing through me right now? What destruction makes space for new growth?",
    },
    "Punarvasu": {
        "affirmation": "I return to myself. Again and again, I come home.",
        "ritual": "Create a small sanctuary today — a corner, a chair, a mat — that represents safety and return. Sit in it for 10 minutes doing nothing.",
        "journal_prompt": "Where is home for me — not a place, but a state of being? What brings me back to my center when I have lost it?",
    },
    "Pushya": {
        "affirmation": "I nourish and am nourished. The river flows both ways.",
        "ritual": "Make food for someone you love — or receive food from someone with full gratitude. Nourishment is a sacrament today.",
        "journal_prompt": "Who or what truly nourishes my spirit? Am I giving my energy to sources that nourish me back?",
    },
    "Ashlesha": {
        "affirmation": "I see clearly. Wisdom rises from the depths of my awareness.",
        "ritual": "Practice deep listening today — to your body, to nature, to a person. Hold what you hear without immediately responding.",
        "journal_prompt": "What hidden truth is asking to be acknowledged? What do I know but have been unwilling to say, even to myself?",
    },
    "Magha": {
        "affirmation": "I carry the fire of my ancestors. Their strength lives in me.",
        "ritual": "Honor your lineage. Place a photo of an ancestor, light a candle, and sit in gratitude for the lives that made yours possible.",
        "journal_prompt": "What did my ancestors pass down that serves me? What legacy am I building that will serve those who come after?",
    },
    "Purva Phalguni": {
        "affirmation": "I rest in beauty. I deserve pleasure, ease, and delight.",
        "ritual": "Do something purely for pleasure today — music, sensory beauty, laughter. Allow yourself to receive enjoyment without guilt.",
        "journal_prompt": "Where in my life have I been denying myself rest or pleasure? What would it mean to let myself truly enjoy being alive?",
    },
    "Uttara Phalguni": {
        "affirmation": "I honor my commitments. Partnership is my sacred practice.",
        "ritual": "Reach out to a partner, friend, or ally and offer something concrete — your time, your skill, your care. Honor a bond.",
        "journal_prompt": "What partnership in my life is calling for deeper commitment? Where have I been taking a relationship for granted?",
    },
    "Hasta": {
        "affirmation": "My hands are my medicine. I create healing with what I make.",
        "ritual": "Work with your hands today — crafting, writing by hand, cooking, massage, or gardening. Let the tactile be meditative.",
        "journal_prompt": "What am I crafting with my life right now? What would I build if I trusted my skills completely?",
    },
    "Chitra": {
        "affirmation": "I am the artist of my own existence. My life is my greatest creation.",
        "ritual": "Create something beautiful today — even something small and impermanent. Arrange flowers, draw a symbol, photograph light.",
        "journal_prompt": "What part of my life feels unbeautiful or unfinished? How might I approach it as an artist rather than a problem-solver?",
    },
    "Swati": {
        "affirmation": "I bend without breaking. Flexibility is my deepest strength.",
        "ritual": "Spend time in open air and wind today. Practice yoga or any stretching that teaches the body softness and range.",
        "journal_prompt": "Where am I being too rigid? What would open up if I became more flexible — in my plans, my opinions, or my identity?",
    },
    "Vishakha": {
        "affirmation": "I am a focused flame. Purpose carries me through every obstacle.",
        "ritual": "Write your single most important goal on paper. Carry it with you today as a reminder of what you are moving toward.",
        "journal_prompt": "What am I most deeply committed to becoming or achieving? Are my daily actions aligned with that commitment?",
    },
    "Anuradha": {
        "affirmation": "I devote myself to what I love. Devotion is the path.",
        "ritual": "Spend time today in devotion to something greater than yourself — prayer, a spiritual practice, service, or simply deep appreciation.",
        "journal_prompt": "What am I devoted to? Does my life reflect my devotion, or am I living divided from what I hold sacred?",
    },
    "Jyeshtha": {
        "affirmation": "I am sovereign. I protect what is sacred with mature authority.",
        "ritual": "Take a walk alone today and consciously claim your inner authority. Speak aloud one boundary you are ready to enforce.",
        "journal_prompt": "Where do I need to step into leadership — in my own life, my relationships, or my community? What responsibility am I ready to take?",
    },
    "Mula": {
        "affirmation": "I go to the root. What falls away reveals what is true.",
        "ritual": "Spend time in nature near the earth — sitting on the ground, touching roots or stone. Let the dissolution be welcome.",
        "journal_prompt": "What in my life is in the process of ending or uprooting? What deeper truth is becoming visible as the surface dissolves?",
    },
    "Purva Ashadha": {
        "affirmation": "I am invincible in my authentic nature. I cannot be touched at the core.",
        "ritual": "Spend time near water — ocean, river, rain. Let the element purify and restore your sense of inner invincibility.",
        "journal_prompt": "What aspect of myself remains undefeated, no matter what circumstances I have faced? What is my indestructible core?",
    },
    "Uttara Ashadha": {
        "affirmation": "I achieve. My victories are earned and lasting.",
        "ritual": "Honor a real achievement in your life today — however small. Write it down. Let yourself receive the recognition you would give another.",
        "journal_prompt": "What victory am I working toward? What would enduring, meaningful success look like in my life — not impressive to others, but deeply right for me?",
    },
    "Shravana": {
        "affirmation": "I listen. The universe is always speaking to those who are still.",
        "ritual": "Spend 20 minutes in deliberate listening — to music, to nature, to silence, to another person. No phone, no multitasking. Just listening.",
        "journal_prompt": "What am I being called to hear right now? What message have I been too busy or too afraid to receive?",
    },
    "Dhanishtha": {
        "affirmation": "I move with rhythm and abundance. The beat of life carries me.",
        "ritual": "Dance, drum, or listen to powerful, rhythmic music today. Let your body find its own natural cadence.",
        "journal_prompt": "Where in my life do I feel out of rhythm? What would it take to reconnect with my natural flow?",
    },
    "Shatabhisha": {
        "affirmation": "I am the healer who walks between worlds. My vision reaches far.",
        "ritual": "Spend time alone under the open sky — day or night. Look at the stars or the horizon. Contemplate the vastness you are part of.",
        "journal_prompt": "What am I here to heal — in myself, in my lineage, or in my community? What visionary gift am I still afraid to fully claim?",
    },
    "Purva Bhadrapada": {
        "affirmation": "I move between fire and wisdom. I transform through the sacred fire of intention.",
        "ritual": "Sit with a candle or fire and contemplate what you are willing to sacrifice for your highest growth. Speak your offering aloud.",
        "journal_prompt": "What must I let burn in order to become who I am meant to be? What sacrifice would free me?",
    },
    "Uttara Bhadrapada": {
        "affirmation": "I rest in the depths. The ocean of wisdom sustains me.",
        "ritual": "Spend time near water or in a bath. Practice yoga nidra or deep rest. Let the depth beneath your thoughts become accessible.",
        "journal_prompt": "What is the wisdom I carry from the deep places I have been — loss, silence, darkness, transformation? How does that wisdom serve others?",
    },
    "Revati": {
        "affirmation": "I complete with grace. Every ending opens into the eternal.",
        "ritual": "Complete something today — a project, a conversation, a habit, a chapter. Honor the completion with a moment of conscious closure.",
        "journal_prompt": "What cycle in my life is completing? What is the gift of this ending — and what new beginning is it making space for?",
    },
}


def get_nakshatra_ritual(nakshatra_name):
    return NAKSHATRA_RITUALS.get(nakshatra_name, {
        "affirmation": f"I align with the energy of {nakshatra_name}.",
        "ritual": "Spend time in quiet reflection, attuning to the lunar energy of today.",
        "journal_prompt": f"What themes of {nakshatra_name} are active in my life right now?",
    })


# ─── Kuta Compatibility Data (Vedic Synastry) ──────────────────────────────────

# Nakshatra Gana (temperament): 1=Deva, 2=Manushya, 3=Rakshasa
NAK_GANA = [
    1, 3, 1, 2, 2, 3, 1, 1, 3,   # Ashwini–Ashlesha
    3, 2, 1, 2, 3, 1, 2, 1, 3,   # Magha–Jyeshtha
    3, 2, 1, 1, 2, 3, 1, 1, 2,   # Mula–Revati
]

# Nakshatra Nadi (energy channel): 1=Vata/Aadi, 2=Pitta/Madhya, 3=Kapha/Antya
NAK_NADI = [
    1, 2, 3, 1, 2, 3, 1, 2, 3,
    1, 2, 3, 1, 2, 3, 1, 2, 3,
    1, 2, 3, 1, 2, 3, 1, 2, 3,
]

# Nakshatra Yoni (animal symbol): 27 nakshatras mapped to 14 animal pairs
NAK_YONI = [
    "horse", "elephant", "sheep", "serpent", "serpent", "dog", "cat", "sheep",
    "cat", "rat", "rat", "cow", "buffalo", "tiger", "buffalo", "tiger",
    "deer", "deer", "dog", "monkey", "mongoose", "cow", "lion", "horse",
    "lion", "cow", "elephant",
]

YONI_COMPATIBILITY = {
    # (animal_a, animal_b) → score 0-4
    # Friendly pairs get 4, neutral 2, enemy 0
    ("horse", "horse"): 4, ("elephant", "elephant"): 4, ("sheep", "sheep"): 4,
    ("serpent", "serpent"): 4, ("dog", "dog"): 4, ("cat", "cat"): 4,
    ("rat", "rat"): 4, ("cow", "cow"): 4, ("buffalo", "buffalo"): 4,
    ("tiger", "tiger"): 4, ("deer", "deer"): 4, ("monkey", "monkey"): 4,
    ("mongoose", "mongoose"): 4, ("lion", "lion"): 4,
    # Natural enemies
    ("dog", "deer"): 0, ("deer", "dog"): 0,
    ("cat", "rat"): 0, ("rat", "cat"): 0,
    ("cow", "tiger"): 0, ("tiger", "cow"): 0,
    ("elephant", "lion"): 0, ("lion", "elephant"): 0,
    ("mongoose", "serpent"): 0, ("serpent", "mongoose"): 0,
}

# Nakshatra Tara (star count) compatibility
def _tara_score(nak_a, nak_b):
    diff = (nak_b - nak_a) % 9 + 1
    good = {1, 3, 5, 7}
    return 3 if diff in good else 0

# Planet friendship table for Graha Maitri
PLANET_FRIENDS = {
    "Sun":     ["Moon", "Mars", "Jupiter"],
    "Moon":    ["Sun", "Mercury"],
    "Mercury": ["Sun", "Venus"],
    "Venus":   ["Mercury", "Saturn"],
    "Mars":    ["Sun", "Moon", "Jupiter"],
    "Jupiter": ["Sun", "Moon", "Mars"],
    "Saturn":  ["Mercury", "Venus"],
}

NAK_LORDS_ORDER = ["Ketu", "Venus", "Sun", "Moon", "Mars", "Rahu", "Jupiter", "Saturn", "Mercury"]


def _nak_lord(nak_idx):
    return NAK_LORDS_ORDER[nak_idx % 9]


def _graha_maitri_score(lord_a, lord_b):
    friends_a = PLANET_FRIENDS.get(lord_a, [])
    friends_b = PLANET_FRIENDS.get(lord_b, [])
    if lord_b in friends_a and lord_a in friends_b:
        return 5
    if lord_b in friends_a or lord_a in friends_b:
        return 3
    return 0


def calculate_kuta_score(moon_nak_a, moon_nak_b, sun_sign_a=None, sun_sign_b=None):
    """
    Calculate Vedic Kuta compatibility score.
    Returns dict with individual scores and total (max 36).
    """
    scores = {}

    # 1. Varna (caste compatibility) — max 1pt
    # Simplified: same varna group = 1, adjacent = 0
    varna = [3, 1, 2, 1, 3, 2, 2, 3, 1, 1, 2, 3, 3, 2, 1, 2, 3, 1, 1, 2, 3, 3, 1, 2, 1, 3, 2]
    scores["varna"] = 1 if varna[moon_nak_a % 27] == varna[moon_nak_b % 27] else 0

    # 2. Vashya (control/attraction) — max 2pt
    # Simplified: same sign group = 2
    vashya_groups = {
        "quadruped": [0, 1, 5, 9, 10],   # Aries, Taurus, Virgo, Cap, Aquarius
        "biped":     [2, 3, 6, 11],        # Gemini, Cancer, Libra, Pisces
        "water":     [3, 7, 11],           # Cancer, Scorpio, Pisces
        "insect":    [5],                  # Virgo
        "wild":      [4, 8],               # Leo, Sagittarius
    }
    nak_sign_a = (moon_nak_a * 360 // 27) // 30
    nak_sign_b = (moon_nak_b * 360 // 27) // 30
    vashya_score = 0
    for grp_signs in vashya_groups.values():
        if nak_sign_a in grp_signs and nak_sign_b in grp_signs:
            vashya_score = 2
            break
        elif nak_sign_a in grp_signs or nak_sign_b in grp_signs:
            vashya_score = 1
            break
    scores["vashya"] = vashya_score

    # 3. Tara (star compatibility) — max 3pt
    scores["tara"] = _tara_score(moon_nak_a, moon_nak_b)

    # 4. Yoni (animal compatibility) — max 4pt
    yoni_a = NAK_YONI[moon_nak_a % 27]
    yoni_b = NAK_YONI[moon_nak_b % 27]
    scores["yoni"] = YONI_COMPATIBILITY.get((yoni_a, yoni_b), 2)

    # 5. Graha Maitri (planet friendship) — max 5pt
    lord_a = _nak_lord(moon_nak_a)
    lord_b = _nak_lord(moon_nak_b)
    scores["graha_maitri"] = _graha_maitri_score(lord_a, lord_b)

    # 6. Gana (temperament) — max 6pt
    gana_a = NAK_GANA[moon_nak_a % 27]
    gana_b = NAK_GANA[moon_nak_b % 27]
    if gana_a == gana_b:
        scores["gana"] = 6
    elif abs(gana_a - gana_b) == 1:
        scores["gana"] = 3
    else:
        scores["gana"] = 0

    # 7. Bhakoot (sign compatibility) — max 7pt
    sign_diff = abs(nak_sign_a - nak_sign_b) % 12
    bhakoot_good = {1, 3, 5, 7, 9, 11}  # 2, 12 or 5, 9 are problematic
    scores["bhakoot"] = 7 if sign_diff in bhakoot_good else 0

    # 8. Nadi (energy/pulse) — max 8pt
    nadi_a = NAK_NADI[moon_nak_a % 27]
    nadi_b = NAK_NADI[moon_nak_b % 27]
    scores["nadi"] = 8 if nadi_a != nadi_b else 0

    total = sum(scores.values())
    max_score = 36

    # Interpretation
    if total >= 28:
        verdict = "Exceptional compatibility — a deeply harmonious union"
    elif total >= 21:
        verdict = "Good compatibility — a supportive and balanced partnership"
    elif total >= 18:
        verdict = "Average compatibility — effort and understanding bridge the differences"
    else:
        verdict = "Challenging compatibility — requires conscious work and mutual growth"

    return {
        "scores": scores,
        "total":  total,
        "max":    max_score,
        "percent": round(total / max_score * 100),
        "verdict": verdict,
        "yoni_animals": {"a": yoni_a, "b": yoni_b},
        "gana":  {"a": gana_a, "b": gana_b},
        "lords": {"a": lord_a, "b": lord_b},
    }

# ══════════════════════════════════════════════════════════════════════════════
# YOGA DATA  (Vedic planetary combinations)
# ══════════════════════════════════════════════════════════════════════════════

YOGA_DATA = {
    # ── Pancha Mahapurusha Yogas ──────────────────────────────────────────
    "Ruchaka Yoga": {
        "type": "Mahapurusha", "color": "red", "icon": "♂", "rarity": "rare",
        "tagline": "The yoga of the great warrior — Mars in full strength at an angular house.",
        "description": (
            "Ruchaka Yoga forms when Mars occupies one of the four angular houses (1st, 4th, 7th, or 10th) "
            "in its own sign (Aries or Scorpio) or sign of exaltation (Capricorn). "
            "Mars at peak power in the chart's most powerful positions creates a person of exceptional physical "
            "and martial energy. The ancient texts describe such a person as having a physique like a lion, "
            "fearless in adversity, and capable of commanding others through sheer force of will and vitality."
        ),
        "effects": [
            "Exceptional physical strength, stamina, and athletic ability",
            "Fearlessness and natural courage in the face of adversity",
            "Leadership in military, law enforcement, surgery, or competitive fields",
            "Potential for property and land gains through decisive action",
            "Fame and recognition for courageous deeds",
        ],
    },
    "Bhadra Yoga": {
        "type": "Mahapurusha", "color": "green", "icon": "☿", "rarity": "rare",
        "tagline": "The yoga of the great intellectual — Mercury at full strength in an angular house.",
        "description": (
            "Bhadra Yoga arises when Mercury is placed in Gemini or Virgo (its own or exaltation sign) "
            "in an angular house (1st, 4th, 7th, or 10th). Mercury is the planet of intelligence, communication, "
            "and commerce, and when it reaches this peak configuration, the native is gifted with a razor-sharp "
            "mind, eloquent speech, and a remarkable capacity for learning and synthesis. The texts describe "
            "such a person as resembling a lion in face, with hands and feet marked by auspicious signs."
        ),
        "effects": [
            "Exceptional intelligence, memory, and analytical ability",
            "Eloquent speech and mastery of language or writing",
            "Success in business, trade, and commercial ventures",
            "Long life and good physical constitution",
            "Fame through intellectual or communicative achievements",
        ],
    },
    "Hamsa Yoga": {
        "type": "Mahapurusha", "color": "gold", "icon": "♃", "rarity": "very_rare",
        "tagline": "The yoga of the great sage — Jupiter at full strength in an angular house.",
        "description": (
            "Hamsa Yoga is formed when Jupiter occupies Sagittarius or Pisces (its own signs) or Cancer "
            "(its exaltation sign) in an angular house. Jupiter is the planet of dharma, wisdom, and spiritual "
            "grace, and this configuration blesses the native with a deeply ethical nature, natural wisdom, "
            "and an almost magnetic spiritual authority. Such individuals become teachers, guides, and pillars "
            "of their community — their lives become a lesson in living with integrity."
        ),
        "effects": [
            "Deep wisdom, philosophical insight, and natural spiritual authority",
            "Success through dharmic and ethical paths",
            "Blessed with a large, loyal, and fortunate circle of supporters",
            "Excellence in teaching, law, philosophy, or spiritual guidance",
            "Prosperity that arrives through righteous means",
        ],
    },
    "Malavya Yoga": {
        "type": "Mahapurusha", "color": "rose", "icon": "♀", "rarity": "rare",
        "tagline": "The yoga of beauty and grace — Venus at full strength in an angular house.",
        "description": (
            "Malavya Yoga is created when Venus is placed in Taurus or Libra (its own signs) or Pisces "
            "(its exaltation sign) in an angular house (1st, 4th, 7th, or 10th). Venus at this level of "
            "strength brings extraordinary grace, aesthetic sensitivity, and magnetic personal charm. "
            "The native is often physically beautiful, naturally cultured, and draws love, luxury, and "
            "creative fulfillment almost effortlessly into their life."
        ),
        "effects": [
            "Physical beauty, personal grace, and natural magnetism",
            "Artistic talent and creative excellence across multiple mediums",
            "Romantic good fortune and deeply satisfying relationships",
            "Enjoyment of fine arts, music, luxury, and material pleasures",
            "Success in beauty, entertainment, design, or diplomacy",
        ],
    },
    "Sasa Yoga": {
        "type": "Mahapurusha", "color": "blue", "icon": "♄", "rarity": "rare",
        "tagline": "The yoga of the ascetic leader — Saturn at full strength in an angular house.",
        "description": (
            "Sasa Yoga occurs when Saturn occupies Capricorn or Aquarius (its own signs) or Libra "
            "(its exaltation sign) in an angular house. Saturn is the great disciplinarian and karmic "
            "teacher, and when it reaches this power, it creates leaders of the masses — people who rise "
            "through relentless effort, patience, and a structural intelligence that can organise large "
            "institutions and communities. Such individuals often hold authority over forests, mines, or "
            "the working classes."
        ),
        "effects": [
            "Authority over large groups, institutions, or systems",
            "Success through discipline, perseverance, and methodical effort",
            "Mastery of legal, administrative, or structural domains",
            "Longevity and sustained achievement over decades",
            "Leadership respected for fairness and systematic thinking",
        ],
    },
    # ── Raja Yogas ──────────────────────────────────────────────────────────
    "Gaja Kesari Yoga": {
        "type": "Raja", "color": "gold", "icon": "♃", "rarity": "common",
        "tagline": "Fame like the elephant-lion — Jupiter in a powerful position from the Moon.",
        "description": (
            "Gaja Kesari (elephant-lion) Yoga forms when Jupiter is in a kendra house (1st, 4th, 7th, or 10th) "
            "from the Moon's position. Since the Moon represents the mind and Jupiter represents wisdom and "
            "fortune, this combination creates a native whose intelligence is both expansive and grounded. "
            "The texts say such a person is famous in their time, respected by the learned, and endowed with "
            "a quality of genuine wisdom that inspires those around them."
        ),
        "effects": [
            "Fame, recognition, and a powerful public reputation",
            "Blessed with wise, helpful, and influential friends and advisors",
            "Success in education, law, philosophy, or any dharmic profession",
            "A life marked by good fortune arriving at key turning points",
            "Natural ability to inspire, guide, and uplift others",
        ],
    },
    "Budha Aditya Yoga": {
        "type": "Raja", "color": "gold", "icon": "☉", "rarity": "common",
        "tagline": "Intelligence illuminated by solar power — Sun and Mercury united.",
        "description": (
            "Budha Aditya Yoga is formed by the conjunction of the Sun (soul, authority) and Mercury "
            "(intellect, communication) in the same house. The combination of solar will with mercurial "
            "intelligence creates a person of brilliant, decisive thinking who can communicate their ideas "
            "with both authority and precision. The native often earns favor from those in power and excels "
            "in any field requiring both clear thinking and confident self-expression."
        ),
        "effects": [
            "Sharp, authoritative intelligence and decisive thinking",
            "Eloquence and persuasive communication skills",
            "Favor from government, authorities, and powerful figures",
            "Success in administration, law, politics, or media",
            "A well-known reputation built on competence and clarity",
        ],
    },
    "Dharma Karma Adhipati Yoga": {
        "type": "Raja", "color": "gold", "icon": "✦", "rarity": "rare",
        "tagline": "Career aligned with dharma — lords of the 9th and 10th in mutual strength.",
        "description": (
            "This profound Raja Yoga forms when the lord of the 9th house (dharma, fortune) and the lord "
            "of the 10th house (karma, career, public status) are conjunct, in mutual aspect, or each "
            "placed in the other's house. It creates a person whose life work is genuinely aligned with "
            "their soul's purpose — success comes not just through ambition, but through right action. "
            "This is the yoga of the person whose profession is also their calling."
        ),
        "effects": [
            "Career that is both externally successful and internally meaningful",
            "Fortune arrives through ethical, purposeful action",
            "Public recognition and prestigious reputation",
            "Strong relationship with spiritual or philosophical guidance",
            "Legacy and lasting impact beyond personal gain",
        ],
    },
    "Neecha Bhanga Raja Yoga": {
        "type": "Raja", "color": "violet", "icon": "△", "rarity": "rare",
        "tagline": "Triumph born from adversity — debilitation cancelled and transformed into strength.",
        "description": (
            "Neecha Bhanga Raja Yoga (cancellation of debilitation, producing royalty) forms when a planet "
            "in its sign of debilitation has its debilitation cancelled by specific conditions — such as the "
            "lord of the debilitation sign being in a kendra from the Moon or Ascendant, or an exalted planet "
            "aspecting the debilitated planet. The result is extraordinary: the very area of the chart that "
            "showed weakness becomes the source of the native's greatest resilience and eventual triumph."
        ),
        "effects": [
            "Extraordinary recovery from early-life difficulties or failures",
            "Success that is all the more powerful for having been hard-won",
            "The area of apparent weakness becomes a signature strength",
            "Rise to prominence after a period of struggle or obscurity",
            "Deep character forged through adversity",
        ],
    },
    "Viparita Raja Yoga": {
        "type": "Raja", "color": "violet", "icon": "⟲", "rarity": "rare",
        "tagline": "Victory through the house of hardship — lords of difficult houses placed in each other's domain.",
        "description": (
            "Viparita (reversed) Raja Yoga forms when the lords of the 6th, 8th, or 12th houses "
            "(the dusthana or difficult houses) are placed in each other's houses or conjunct each other. "
            "Through a paradoxical mechanism, the energies of difficulty cancel each other out and produce "
            "success. The native often achieves power through their ability to work with what others cannot — "
            "hidden knowledge, foreign connections, health crises, or inheritance."
        ),
        "effects": [
            "Success through unconventional, unexpected, or hidden paths",
            "Gains from situations that defeat most others",
            "Ability to turn enemies, obstacles, and losses into advantages",
            "Power in fields related to research, healing, or the occult",
            "A life trajectory that confounds conventional expectations",
        ],
    },
    # ── Auspicious Yogas ──────────────────────────────────────────────────
    "Adhi Yoga": {
        "type": "Auspicious", "color": "green", "icon": "♃", "rarity": "rare",
        "tagline": "Benefics surrounding the mind — Mercury, Venus, and Jupiter in powerful positions from Moon.",
        "description": (
            "Adhi Yoga forms when natural benefics (Mercury, Venus, Jupiter) occupy the 6th, 7th, and 8th "
            "houses from the Moon. This places benefic energy all around the lunar mind, creating a person "
            "whose mental world is surrounded by support, beauty, and wisdom. The texts describe such a "
            "native as becoming a minister, commander, or leader — someone who is cherished by their "
            "community and achieves success through inner resources rather than raw aggression."
        ),
        "effects": [
            "Natural leadership capacity that earns genuine affection",
            "Good health, long life, and physical wellbeing",
            "Success over adversaries without resorting to conflict",
            "Surrounded by helpful, cultured, and wise friends",
            "Mental balance, emotional resilience, and psychological strength",
        ],
    },
    "Amala Yoga": {
        "type": "Auspicious", "color": "green", "icon": "☽", "rarity": "common",
        "tagline": "An unblemished reputation — a natural benefic in the 10th house from Ascendant or Moon.",
        "description": (
            "Amala Yoga (the yoga of purity) forms when a natural benefic planet (Jupiter, Venus, or Mercury) "
            "is placed in the 10th house from either the Ascendant or the Moon. Since the 10th house governs "
            "career, public image, and one's actions in the world, the presence of a benefic here ensures "
            "that the native's reputation remains spotless. Their professional life is characterized by "
            "integrity, and their fame endures long after they leave the stage."
        ),
        "effects": [
            "Lasting, spotless reputation and public honor",
            "Success in profession through ethical, righteous means",
            "Fame that endures and grows over time",
            "Natural capacity to inspire others by example",
            "Work recognized as genuinely beneficial to society",
        ],
    },
    "Kesari Yoga": {
        "type": "Auspicious", "color": "gold", "icon": "♃", "rarity": "common",
        "tagline": "Lion-like fortune — Jupiter in a kendra from the Ascendant.",
        "description": (
            "Kesari (lion) Yoga forms when Jupiter occupies an angular house (1st, 4th, 7th, or 10th) "
            "from the Ascendant. Jupiter in these powerful structural positions bestows its expansive "
            "blessings directly onto the frame of the life — the body, home, partnerships, and career "
            "all benefit. This is one of the most broadly positive yoga configurations, giving the native "
            "a fundamentally optimistic, wise, and fortunate orientation to life."
        ),
        "effects": [
            "Broad good fortune and an optimistic, expansive life",
            "Success in education, law, philosophy, or spiritual work",
            "Respected and favored by wise and powerful people",
            "Financial stability and comfortable living",
            "A life of genuine meaning and ethical grounding",
        ],
    },
    "Vesi Yoga": {
        "type": "Auspicious", "color": "gold", "icon": "☉", "rarity": "common",
        "tagline": "Benefic in the solar 2nd house — strengthened wealth, speech, and career.",
        "description": (
            "Vesi Yoga forms when any planet other than the Moon occupies the 2nd house from the Sun. "
            "The 2nd from the Sun relates to accumulated solar energy and what follows one's solar purpose — "
            "typically affecting wealth, speech, and career momentum. When a benefic planet occupies this "
            "position, it amplifies the flow of fortune and eloquence from the Sun's house outward."
        ),
        "effects": [
            "Fortunate speech — words that carry weight and open doors",
            "Career momentum that builds steadily over time",
            "Financial gains through professional effort",
            "Good character and principled actions recognized publicly",
            "Assistance from authority figures and solar-type mentors",
        ],
    },
    "Shubha Kartari Yoga": {
        "type": "Auspicious", "color": "green", "icon": "✦", "rarity": "common",
        "tagline": "Protected by benefics on both sides — natural grace and good fortune at the Ascendant.",
        "description": (
            "Shubha Kartari (benefic scissors) Yoga forms when natural benefic planets (Jupiter, Venus, "
            "Mercury, or waxing Moon) occupy both the 2nd and 12th houses from the Ascendant, flanking "
            "it like protective wings. The Ascendant — representing the self, body, and life force — is "
            "surrounded and supported by benevolent energies, creating a person of natural charm, "
            "good health, and a fundamentally fortunate life experience."
        ),
        "effects": [
            "Natural physical grace, health, and personal magnetism",
            "Surrounded by positive environments and supportive people",
            "A fundamentally fortunate and well-supported life",
            "Balanced temperament and emotional resilience",
            "Ease in self-expression and confident identity",
        ],
    },
    "Saraswati Yoga": {
        "type": "Auspicious", "color": "violet", "icon": "♃", "rarity": "very_rare",
        "tagline": "Blessed by the goddess of wisdom — the intellectual triumvirate of Jupiter, Venus, and Mercury aligned.",
        "description": (
            "Saraswati Yoga (named for the goddess of arts, wisdom, and learning) forms when Jupiter, "
            "Venus, and Mercury are all placed in kendras, trikonas, or the 2nd house in their own or "
            "exalted signs. This rare alignment brings together the three planets most associated with "
            "intelligence, creativity, and wisdom in their most powerful configurations. The result is "
            "a genuinely exceptional mind with the capacity for mastery across intellectual and creative domains."
        ),
        "effects": [
            "Extraordinary intellectual and creative gifts",
            "Mastery of arts, music, literature, or multiple academic fields",
            "Fame and recognition through creative or intellectual work",
            "Eloquent expression in both artistic and analytical registers",
            "A life genuinely devoted to and rewarded by the pursuit of knowledge",
        ],
    },
    "Parivartana Yoga": {
        "type": "Exchange", "color": "violet", "icon": "⟷", "rarity": "common",
        "tagline": "Mutual reception — two planets inhabit each other's signs, deeply interweaving their energies.",
        "description": (
            "Parivartana (exchange) Yoga occurs when two planets occupy each other's ruling signs, "
            "creating a powerful mutual reception. Each planet acts as if it were in its own sign, "
            "while simultaneously strengthening the other. This weaves the two planets' themes "
            "inextricably together in the native's life — the houses they rule become intimately "
            "connected, and the native often achieves strength in both areas simultaneously."
        ),
        "effects": [
            "The two exchanging planets and their houses operate as a unified force",
            "Strength and activity in both houses governed by the exchanging planets",
            "Events in one area of life consistently catalyse the other",
            "The native is known for bridging the themes these two planets represent",
            "A sense that two seemingly separate life domains are deeply the same thing",
        ],
    },
    # ── Challenging Yogas ────────────────────────────────────────────────
    "Kemadruma Yoga": {
        "type": "Challenging", "color": "muted", "icon": "☽", "rarity": "common",
        "tagline": "The isolated Moon — no planetary support in the 2nd or 12th from the Moon.",
        "description": (
            "Kemadruma Yoga forms when no planet occupies the 2nd or 12th house from the Moon, "
            "leaving the mind isolated from planetary support. The Moon represents the mind, emotions, "
            "and social nature, and when it sits alone without neighboring planets, the native may "
            "experience periods of isolation, self-doubt, or difficulty finding sustained support. "
            "This is a yoga that calls for inner development — and it is cancelled by several "
            "conditions including a planet in a kendra from the Moon."
        ),
        "effects": [
            "Periods of emotional isolation or feelings of operating alone",
            "Inner self-reliance developed through necessity",
            "Potential financial or social instability at certain life periods",
            "Deep inner life developed through solitude",
            "Cancelled if planets are in kendras from Moon — check your full chart",
        ],
    },
    "Chandra Mangala Yoga": {
        "type": "Dhana", "color": "red", "icon": "☽", "rarity": "common",
        "tagline": "The bold emotional warrior — Moon and Mars conjunct, combining feeling and action.",
        "description": (
            "Chandra Mangala Yoga forms when the Moon and Mars occupy the same house. "
            "The Moon's emotional sensitivity and Mars's raw drive create a powerful, "
            "emotionally-fuelled ambition. This combination produces acute business instincts, "
            "real estate savvy, and financial boldness. The native acts on feeling-based intelligence "
            "and often succeeds through industries related to land, food, liquids, or physical products. "
            "The challenge is managing emotional reactivity and impulsiveness."
        ),
        "effects": [
            "Strong financial instincts and business acumen",
            "Success in real estate, food, hospitality, or physical products",
            "Bold emotional nature that drives decisive action",
            "Gains through mother, property, or agricultural ventures",
            "Passionate personality — both in love and in business",
        ],
    },
}


def get_yoga_data(name):
    return YOGA_DATA.get(name, {})


# ══════════════════════════════════════════════════════════════════════════════
# PLANETARY ASPECT INTERPRETATIONS  (Graha Drishti)
# ══════════════════════════════════════════════════════════════════════════════

# Format: ASPECT_INTERP[aspecting_planet][aspected_planet] = text
ASPECT_INTERP = {
    "Sun": {
        "Moon":    "Sun aspecting Moon illuminates the emotional nature with solar authority. The heart and the identity are deeply linked — public life and private feelings are hard to separate. There is a strong pull toward recognition, and emotions often fuel ambition.",
        "Mercury": "Sun aspecting Mercury sharpens the intellect with solar will. Thought and identity merge — the native thinks as they are, making them convincing communicators and decisive analysts.",
        "Venus":   "Sun aspecting Venus can create tension between ego and love. The desire for admiration may complicate intimate relationships, yet it also drives artistic ambition and a need to create beauty that reflects the self.",
        "Mars":    "Sun aspecting Mars creates an intense, competitive fire. Willpower and drive amplify each other — great courage, athletic ability, and competitive success, but a tendency toward anger or confrontation.",
        "Jupiter": "Sun aspecting Jupiter is one of the most auspicious combinations — the soul's purpose aligns with wisdom and grace. This aspect brings good fortune, authority, and a magnanimous character recognized by the powerful.",
        "Saturn":  "Sun aspecting Saturn is a demanding aspect — the ego meets the disciplinarian. This creates a serious, hardworking, and often high-achieving individual who must earn everything through sustained effort. Early life may be austere.",
        "Rahu":    "Sun aspecting Rahu creates worldly ambition tinged with compulsion. The native's identity and desires intensify each other — there is great drive for success, but a risk of going too far in pursuit of recognition.",
        "Ketu":    "Sun aspecting Ketu brings the soul into contact with past-life themes. There is a spiritual pull that sometimes conflicts with worldly ambition — the native's identity is shaped by renunciation as much as attainment.",
    },
    "Moon": {
        "Sun":     "Moon aspecting Sun sensitises the will with emotion. The native's actions are deeply personal and feeling-driven — their public life is a direct expression of their inner state.",
        "Mercury": "Moon aspecting Mercury blends intuition with intellect. The native thinks with emotional intelligence — they are perceptive communicators and often gifted writers, counselors, or teachers.",
        "Venus":   "Moon aspecting Venus is a beautifying, loving aspect — the emotional nature flows naturally toward harmony and pleasure. Artistic sensitivity is heightened; relationships are warm and affectionate.",
        "Mars":    "Moon aspecting Mars charges the emotions with energy and urgency. The native is emotionally reactive, passionate, and driven. This can fuel great creative and physical output when channeled well.",
        "Jupiter": "Moon aspecting Jupiter is profoundly auspicious — wisdom and emotional grace combine. The native is generous, optimistic, and respected; good fortune arrives through emotional generosity and genuine care.",
        "Saturn":  "Moon aspecting Saturn creates emotional discipline through difficulty. The inner life may feel constrained or serious; however, sustained emotional work leads to profound psychological depth and maturity.",
        "Rahu":    "Moon aspecting Rahu creates emotional intensity around desire and obsession. The mind can run in restless loops; the native's emotional life is entangled with worldly ambition and unfulfilled longing.",
        "Ketu":    "Moon aspecting Ketu creates a deeply psychic and detached emotional nature. The native has unusual perceptual sensitivity, spiritual dreams, and a capacity for emotional wisdom that transcends the ordinary.",
    },
    "Mercury": {
        "Sun":     "Mercury aspecting Sun sharpens communication with purpose. Words carry authority; the native writes and speaks in ways that shape outcomes.",
        "Moon":    "Mercury aspecting Moon creates a mind that thinks in feelings. Perceptive, empathic communication — excellent in counseling, creative writing, and psychology.",
        "Venus":   "Mercury aspecting Venus is the aspect of the artist-intellectual. Aesthetic intelligence and communicative grace combine — success in design, writing, music, or diplomacy.",
        "Mars":    "Mercury aspecting Mars gives intellectual boldness. Arguments are sharp and decisive; the native debates, negotiates, and competes with strategic intelligence.",
        "Jupiter": "Mercury aspecting Jupiter creates the scholar — vast intellectual hunger combined with wisdom and ethical grounding. Excellence in philosophy, law, teaching, and publishing.",
        "Saturn":  "Mercury aspecting Saturn creates methodical, precise thought. The native is a careful, disciplined thinker — slow to conclude but highly accurate. Success in science, engineering, or administration.",
        "Rahu":    "Mercury aspecting Rahu creates a brilliant but potentially obsessive mind. The intellect runs fast and far — excellent for research, technology, and unconventional innovation.",
        "Ketu":    "Mercury aspecting Ketu creates intuitive, non-linear intelligence. The native's mind connects dots others miss — excellent in spirituality, healing arts, or mystical traditions.",
    },
    "Venus": {
        "Sun":     "Venus aspecting Sun refines the personality with grace and aesthetic awareness. The native radiates charm; success comes through personal magnetism and cultural polish.",
        "Moon":    "Venus aspecting Moon is exquisitely harmonious — beauty and emotion flow together. The native craves and creates emotional beauty; deeply loving, artistic, and sensually alive.",
        "Mercury": "Venus aspecting Mercury creates the gifted communicator of beauty — poets, designers, diplomats, and artists who speak the language of harmony.",
        "Mars":    "Venus aspecting Mars is the aspect of passionate love and creative drive. Intense romantic life; artistic work infused with bold energy. The challenge is balancing desire with stability.",
        "Jupiter": "Venus aspecting Jupiter is one of the most fortunate aspects for pleasure and prosperity. The native is naturally generous, well-liked, and often blessed with both love and material abundance.",
        "Saturn":  "Venus aspecting Saturn disciplines love and pleasure. Relationships require patience and realistic commitment. Beauty is earned, not given — but it endures when it arrives.",
        "Rahu":    "Venus aspecting Rahu amplifies desire and romantic compulsion. The love life may be intense, unconventional, or marked by foreign connections. Artistic drive becomes almost obsessive.",
        "Ketu":    "Venus aspecting Ketu creates detachment from material pleasure — a spiritual artist who finds beauty in transcendence. May renounce or lose attachments in pursuit of something deeper.",
    },
    "Mars": {
        "Sun":     "Mars aspecting Sun with its powerful special aspects charges the life with drive and competitive energy. Will and action merge — the native is bold, direct, and physically energetic.",
        "Moon":    "Mars aspecting Moon stirs the emotions to action. The inner life is active and sometimes turbulent; the native is emotionally brave and physically driven.",
        "Mercury": "Mars aspecting Mercury gives intellectual aggression — fast, sharp, cutting debate. Success in strategic fields, law, and any domain requiring competitive thinking.",
        "Venus":   "Mars aspecting Venus heats the love life with passion and intensity. Powerful attraction and creative drive; the challenge is tempering desire with patience.",
        "Jupiter": "Mars aspecting Jupiter combines drive with wisdom. Action guided by dharma — the native is bold but fair, competitive but principled. Success in law, sports, or public leadership.",
        "Saturn":  "Mars aspecting Saturn is the clash of force and discipline. Tremendous constructive potential when integrated; frustration and obstruction when not. The native must learn to build patiently.",
        "Rahu":    "Mars aspecting Rahu creates explosive, compulsive drive. Extraordinary energy and ambition; risk of overreach or accident if not channeled deliberately.",
        "Ketu":    "Mars aspecting Ketu creates a spiritual warrior. Action is driven by an inner calling beyond material gain — the native fights for transcendent purposes.",
    },
    "Jupiter": {
        "Sun":     "Jupiter aspecting Sun with its gracious 9th or 5th special aspects blesses the identity with wisdom and good fortune. The native is respected, ethical, and naturally fortunate.",
        "Moon":    "Jupiter aspecting Moon is one of the most healing aspects in astrology. The mind is expanded, optimistic, and wise. Emotional generosity and good fortune characterize the inner life.",
        "Mercury": "Jupiter aspecting Mercury elevates the intellect with philosophical depth. The native thinks big, speaks with authority, and excels in education, law, or spiritual writing.",
        "Venus":   "Jupiter aspecting Venus blesses love and pleasure with abundance. The native's relationships are warm, expansive, and often fortunate. Artistic work reaches a wide audience.",
        "Mars":    "Jupiter aspecting Mars elevates courage with dharmic purpose. Bold action guided by wisdom — the native achieves great things in ways that benefit others as well as themselves.",
        "Saturn":  "Jupiter aspecting Saturn is a profound and tempering influence on the karmic planet. Hard work is rewarded with wisdom; discipline finds its deeper purpose. An excellent aspect for sustained achievement.",
        "Rahu":    "Jupiter aspecting Rahu brings wisdom and ethical grounding to worldly desire. The native's ambitions are elevated — success through dharmic means rather than shortcuts.",
        "Ketu":    "Jupiter aspecting Ketu creates a deep spiritual philosopher — past-life wisdom infused with present-life dharmic knowledge. A natural teacher of transcendent subjects.",
    },
    "Saturn": {
        "Sun":     "Saturn aspecting Sun with its intense special aspects (3rd, 7th, 10th) tests the identity with discipline and limitation. The native must earn authority through sustained effort — but what they build lasts.",
        "Moon":    "Saturn aspecting Moon creates emotional discipline through difficulty. The inner life is serious and sometimes lonely — but profoundly deep. Emotional resilience forged over time.",
        "Mercury": "Saturn aspecting Mercury creates precision, patience, and methodical intelligence. The native thinks carefully and speaks with measured authority. Success in science, law, engineering.",
        "Venus":   "Saturn aspecting Venus disciplines love and pleasure. Relationships are taken seriously — perhaps delayed, but deeply committed when they arrive. Beauty achieved through effort endures.",
        "Mars":    "Saturn aspecting Mars is a challenging aspect of blocked action. Energy meets resistance — but when integrated, this creates extraordinary productive endurance and disciplined power.",
        "Jupiter": "Saturn aspecting Jupiter is the aspect of the dharmic builder. Expansive wisdom is given structural form — the native builds institutions, systems, and lasting frameworks for good.",
        "Rahu":    "Saturn aspecting Rahu combines karma and compulsion — the native faces intense karmic work around worldly desire. Profound character development through meeting life's hardest lessons.",
        "Ketu":    "Saturn aspecting Ketu creates a deeply spiritual, serious, and somewhat austere inner life. Past-life spiritual discipline is activated; the native is drawn toward monastic or renunciant paths.",
    },
    "Rahu": {
        "Sun":     "Rahu aspecting Sun amplifies the ego with desire and worldly ambition. Great drive for recognition — the native may achieve fame but must guard against hubris.",
        "Moon":    "Rahu aspecting Moon creates mental restlessness, desire, and emotional intensity. The mind is hyper-perceptive; prone to obsession but also exceptional creative insight.",
        "Mercury": "Rahu aspecting Mercury gives unconventional, rapid intelligence. Excellent in technology, research, and innovation — the mind moves fast and far beyond conventional limits.",
        "Venus":   "Rahu aspecting Venus intensifies desire for love, beauty, and pleasure. Magnetic and unconventional in relationships; artistic work is bold and boundary-pushing.",
        "Mars":    "Rahu aspecting Mars creates explosive, compulsive drive. Extraordinary energy for ambition — must be channeled deliberately to avoid recklessness.",
        "Jupiter": "Rahu aspecting Jupiter creates worldly ambition fuelled by a hunger for wisdom or spiritual status. The native may seek gurus, philosophy, or religious authority with unusual intensity.",
        "Saturn":  "Rahu aspecting Saturn intensifies karmic work. The native meets old patterns of restriction with new urgency — profound transformation possible through sustained inner work.",
        "Ketu":    "Rahu aspecting Ketu creates the karmic axis in full expression. The pull between worldly desire and spiritual detachment is the central theme of this lifetime.",
    },
    "Ketu": {
        "Sun":     "Ketu aspecting Sun creates a soul working through identity issues from past lives. The ego is thin and permeable — spiritual depth is natural; worldly ambition may feel hollow.",
        "Moon":    "Ketu aspecting Moon creates psychic sensitivity, spiritual dreams, and emotional detachment. The inner life has access to dimensions beyond the ordinary.",
        "Mercury": "Ketu aspecting Mercury gives intuitive, non-linear intelligence — the native receives insights rather than calculates them. Excellence in spiritual, mystical, or healing traditions.",
        "Venus":   "Ketu aspecting Venus creates detachment from pleasure and a search for transcendent beauty. The native finds conventional love unsatisfying — spiritual connection is what they truly seek.",
        "Mars":    "Ketu aspecting Mars creates a spiritual warrior — action driven by renunciation and inner calling rather than personal gain. Past-life martial skill surfaces in this life.",
        "Jupiter": "Ketu aspecting Jupiter creates a guru of the inner path — past-life wisdom arising naturally in this life. The native may have unusual access to spiritual knowledge.",
        "Saturn":  "Ketu aspecting Saturn creates deep karmic seriousness. The native works through old patterns of discipline and limitation with unusual spiritual purpose.",
        "Rahu":    "Ketu aspecting Rahu keeps the karmic axis in full tension — the native lives the push-pull between attachment and liberation as the central drama of life.",
    },
}


def get_aspect_interpretation(from_planet, to_planet, aspect_num):
    """Return the interpretation for a planet aspecting another."""
    text = ASPECT_INTERP.get(from_planet, {}).get(to_planet, "")
    if not text:
        text = ASPECT_INTERP.get(to_planet, {}).get(from_planet, "")
    if not text:
        text = f"{from_planet} casts its {aspect_num}th-house aspect upon {to_planet}, interweaving their energies in the areas of life these planets govern."
    return text

# ══════════════════════════════════════════════════════════════════════════════
# EXTENDED YOGA DATA
# ══════════════════════════════════════════════════════════════════════════════

YOGA_DATA.update({

    "Sunapha Yoga": {
        "type": "Lunar",
        "color": "blue",
        "icon": "☽",
        "rarity": "common",
        "tagline": "The Moon flanked by fortune — wealth and reputation arise naturally.",
        "description": "Sunapha Yoga forms when one or more planets (other than the Sun) occupy the 2nd house from the Moon. The Moon, representing the mind and public image, is supported from behind by planetary energy, indicating self-made prosperity and an independently earned reputation.",
        "effects": [
            "Self-earned wealth and financial independence",
            "Strong reputation built through personal effort",
            "Resourceful and enterprising mind-set",
            "Good speech and persuasive communication",
            "Success through one's own merit rather than inheritance",
        ],
    },

    "Anapha Yoga": {
        "type": "Lunar",
        "color": "blue",
        "icon": "☽",
        "rarity": "common",
        "tagline": "The Moon sheltered ahead — a gracious, well-provided life.",
        "description": "Anapha Yoga forms when one or more planets (other than the Sun) occupy the 12th house from the Moon. This yoga blesses the native with physical attractiveness, a dignified bearing, and comfort in later years. The mind finds ease and quiet pleasure throughout life.",
        "effects": [
            "Physical beauty and personal magnetism",
            "Dignified, well-mannered conduct",
            "Comfortable and gracious lifestyle",
            "Love of leisure, sensory pleasure, and the arts",
            "Financial ease, especially in the second half of life",
        ],
    },

    "Durudhara Yoga": {
        "type": "Lunar",
        "color": "teal",
        "icon": "☽",
        "rarity": "uncommon",
        "tagline": "The Moon embraced on both sides — a life of wealth and generosity.",
        "description": "Durudhara Yoga forms when planets occupy both the 2nd and 12th houses from the Moon simultaneously (combining Sunapha and Anapha). The mind is surrounded by planetary support on both flanks, producing a generous, wealthy, and socially magnetic individual who is admired for their balanced character.",
        "effects": [
            "Substantial material wealth and financial security",
            "Renowned for generosity and open-handedness",
            "Excellent public image and widespread popularity",
            "Balanced personality — both earns and enjoys freely",
            "Strong social and political influence",
        ],
    },

    "Vasumati Yoga": {
        "type": "Auspicious",
        "color": "green",
        "icon": "♃",
        "rarity": "uncommon",
        "tagline": "Benefics in the houses of growth — material abundance flows steadily.",
        "description": "Vasumati Yoga forms when all three natural benefics (Jupiter, Venus, Mercury) occupy the upachaya houses (3rd, 6th, 10th, or 11th) from the Moon or the Ascendant. Upachaya houses grow stronger over time, so this yoga delivers increasing wealth, influence, and achievement as the native ages.",
        "effects": [
            "Growing wealth and prosperity over the lifetime",
            "Strong career achievements that compound with age",
            "Victory over enemies and competitors",
            "Financial abundance from multiple sources",
            "Increasing respect and authority with age",
        ],
    },

    "Lakshmi Yoga": {
        "type": "Raja",
        "color": "gold",
        "icon": "♀",
        "rarity": "rare",
        "tagline": "The goddess of wealth herself blesses this chart.",
        "description": "Lakshmi Yoga forms when the lord of the 9th house (fortune) is placed in its own sign or exaltation AND occupies a kendra or trikona house. The 9th lord is the primary planet of fortune, and when it is both powerful and well-placed, the goddess Lakshmi — deity of wealth and divine grace — blesses the native directly.",
        "effects": [
            "Extraordinary wealth and material prosperity",
            "Radiant physical beauty and personal charisma",
            "Deep religiosity and adherence to dharma",
            "Royal or government connections and patronage",
            "Long life and excellent health",
            "Fame that outlasts the native's own lifetime",
        ],
    },

    "Guru Mangala Yoga": {
        "type": "Auspicious",
        "color": "orange",
        "icon": "♃♂",
        "rarity": "uncommon",
        "tagline": "Courage meets wisdom — the warrior-philosopher combination.",
        "description": "Guru Mangala Yoga forms when Jupiter and Mars are conjunct in the same sign or in mutual 7th-house aspect. Jupiter brings wisdom, dharma, and grace; Mars brings courage, initiative, and physical power. Together they create a bold, principled individual capable of leading others through difficult terrain.",
        "effects": [
            "Exceptional courage tempered by ethical judgment",
            "Leadership ability in competitive or crisis situations",
            "Success in law, military, sports, or management",
            "Powerful protective instinct for family and principles",
            "Ambition directed toward noble and just causes",
        ],
    },

    "Shakata Yoga": {
        "type": "Challenging",
        "color": "gray",
        "icon": "☽",
        "rarity": "common",
        "tagline": "Fortune rises and falls like a wheel — resilience is the lesson.",
        "description": "Shakata Yoga forms when Jupiter is placed in the 6th, 8th, or 12th house from the Moon (the dusthana houses). Jupiter's expansive benefic energy is muted or blocked by the Moon's adverse angular relationship, causing fluctuating fortune. The native may experience cycles of rise and fall, but those who develop resilience can still achieve much.",
        "effects": [
            "Fluctuating financial fortunes — ups and downs",
            "Periodic setbacks that teach resilience and adaptability",
            "Wisdom gained through difficulty rather than ease",
            "Mid-life or later-life recovery often stronger than early years",
            "Tendency to underestimate one's own potential",
        ],
    },

    "Chamara Yoga": {
        "type": "Raja",
        "color": "purple",
        "icon": "♃",
        "rarity": "rare",
        "tagline": "Honoured like royalty — a life of distinction and scholarly acclaim.",
        "description": "Chamara Yoga forms when the Ascendant lord is exalted and conjunct Jupiter, or when Jupiter itself occupies the Ascendant or 7th house in a strong condition. The native is distinguished by intellectual brilliance, philosophical wisdom, and a regal bearing that earns them recognition from rulers, scholars, and the public alike.",
        "effects": [
            "Scholarly distinction and intellectual reputation",
            "Honoured and celebrated during one's lifetime",
            "Success in teaching, philosophy, law, or governance",
            "Personal magnetism and dignified bearing",
            "Long life with enduring legacy",
        ],
    },

    "Kahala Yoga": {
        "type": "Raja",
        "color": "red",
        "icon": "♂",
        "rarity": "uncommon",
        "tagline": "The yoga of the bold commander — authority through courage.",
        "description": "Kahala Yoga forms when the lords of the 4th and 9th houses are in mutual kendra positions AND the Ascendant lord is strong. The 4th house represents stability and homeland; the 9th represents dharma and fortune. When their lords are in angular relationship to each other, the native becomes a bold, confident commander who leads from strength.",
        "effects": [
            "Natural authority and commanding presence",
            "Success as a leader, administrator, or military figure",
            "Courage and decisiveness in the face of obstacles",
            "Ownership of land, property, or estates",
            "Victory over opposition through boldness",
        ],
    },

    "Maha Bhagya Yoga": {
        "type": "Auspicious",
        "color": "gold",
        "icon": "☀",
        "rarity": "rare",
        "tagline": "Born at the perfect moment — fortune written in the stars.",
        "description": "Maha Bhagya Yoga (Great Luck Yoga) has strict requirements: for males, the Sun, Moon, and Ascendant must all be in odd signs (Aries, Gemini, Leo, Libra, Sagittarius, Aquarius) and the birth must be during the day. For females, all three must be in even signs and the birth at night. When met, this yoga marks a chart of exceptional fortune and good karma.",
        "effects": [
            "Exceptional lifelong fortune and good luck",
            "Born into or rises to positions of influence",
            "Virtuous character that attracts goodwill naturally",
            "Long life with health and happiness",
            "Benefits not just oneself but family and community",
        ],
    },

    "Pushkala Yoga": {
        "type": "Auspicious",
        "color": "teal",
        "icon": "☽",
        "rarity": "uncommon",
        "tagline": "The full, nourished Moon — a prosperous and honoured life.",
        "description": "Pushkala Yoga forms when the Moon is in a friendly sign or its own navamsa, the lord of that sign is in a kendra, and the Ascendant lord is strong. The Moon, full and nourished, bestows comfort, popularity, and material prosperity. This yoga is particularly strong near full moon births.",
        "effects": [
            "Material prosperity and comfortable living",
            "Wide popularity and genuine affection from others",
            "Sensitive, artistic, and emotionally intelligent nature",
            "Success in public-facing careers",
            "Respected and honoured in one's community",
        ],
    },

    "Nipuna Yoga": {
        "type": "Auspicious",
        "color": "blue",
        "icon": "☿",
        "rarity": "uncommon",
        "tagline": "Masterful skill and razor intellect — the expert's yoga.",
        "description": "Nipuna Yoga (also called Budha-Aditya in some traditions, but here specifically) forms when Mercury is exalted or in its own sign AND aspects or conjoins the Ascendant. Mercury's sharp, analytical energy becomes a defining quality of the personality itself — the native is known for intellectual brilliance, technical mastery, and communication skill.",
        "effects": [
            "Exceptional intellectual and technical abilities",
            "Mastery in one's chosen field or craft",
            "Eloquent, persuasive communication",
            "Success in writing, analysis, science, or business",
            "Sharp memory and rapid learning capacity",
        ],
    },

})


# ══════════════════════════════════════════════════════════════════════════════
# SPOUSE / PARTNER PROFILE INTERPRETATIONS
# ══════════════════════════════════════════════════════════════════════════════

# Qualities of the spouse indicated by the 7th lord's sign placement
SPOUSE_SIGN_QUALITIES = {
    "Aries": {
        "personality": "Dynamic, independent, and energetic",
        "traits": ["Bold and action-oriented", "Naturally competitive and driven", "Direct and honest communicator", "Loves adventure and new experiences"],
        "appearance": "Athletic build, confident posture, expressive eyes",
        "meeting": "Through sports, travel, competitive events, or chance encounters that feel electric",
        "challenges": "May be impulsive or impatient; needs space and independence",
    },
    "Taurus": {
        "personality": "Stable, sensual, and deeply loyal",
        "traits": ["Reliable and consistent in commitment", "Appreciates beauty, comfort, and good food", "Patient and steady emotional nature", "Values security and long-term stability"],
        "appearance": "Well-built, warm eyes, naturally attractive, pleasant voice",
        "meeting": "Through creative circles, social gatherings, or introductions by mutual friends",
        "challenges": "Can be stubborn or resistant to change; slow to open emotionally",
    },
    "Gemini": {
        "personality": "Witty, communicative, and intellectually curious",
        "traits": ["Quick-minded and endlessly interesting to talk to", "Adaptable and socially versatile", "Light-hearted but needs mental stimulation", "Youthful energy regardless of age"],
        "appearance": "Slender or lithe build, animated face, expressive hands",
        "meeting": "Through social events, education, writing circles, or digital connections",
        "challenges": "May seem inconsistent or struggle with deep commitment early on",
    },
    "Cancer": {
        "personality": "Nurturing, emotionally deep, and family-oriented",
        "traits": ["Deeply caring and protective of loved ones", "Intuitive and emotionally perceptive", "Strong attachment to home and tradition", "Loyal to the point of self-sacrifice"],
        "appearance": "Soft features, kind eyes, comforting presence",
        "meeting": "Through family connections, domestic settings, or community gatherings",
        "challenges": "Can be overly sensitive or clingy; needs emotional reassurance",
    },
    "Leo": {
        "personality": "Charismatic, generous, and warmly dignified",
        "traits": ["Natural leader with a generous heart", "Loves to be admired and to admire in return", "Loyal and devoted when their pride is respected", "Creative and dramatic flair"],
        "appearance": "Striking presence, radiant smile, often has distinctive hair",
        "meeting": "Through entertainment, creative pursuits, parties, or high-profile social events",
        "challenges": "May need excessive validation or have a strong ego to navigate",
    },
    "Virgo": {
        "personality": "Intelligent, detail-oriented, and quietly devoted",
        "traits": ["Analytical mind with a practical approach to love", "Deeply caring expressed through acts of service", "Health-conscious and organized", "Discriminating taste and high standards"],
        "appearance": "Clean, neat appearance; often slim; refined manner",
        "meeting": "Through work, health settings, intellectual activities, or everyday routines",
        "challenges": "May be critical or overly analytical in relationships; perfectionist tendencies",
    },
    "Libra": {
        "personality": "Charming, harmonious, and naturally gracious",
        "traits": ["Exceptionally fair-minded and considerate", "Aesthetic sensitivity — loves beauty in all forms", "Skilled diplomat and mediator", "Romantic and idealistic about partnership"],
        "appearance": "Naturally attractive and well-groomed; balanced, symmetrical features",
        "meeting": "Through artistic events, social introductions, or professional networking",
        "challenges": "May be indecisive or avoid confrontation at the cost of honesty",
    },
    "Scorpio": {
        "personality": "Intense, magnetic, and deeply transformative",
        "traits": ["All-or-nothing commitment — fully invested or not at all", "Perceptive to the point of reading minds", "Passionately loyal to those they trust", "Drawn to depth, mystery, and hidden truths"],
        "appearance": "Intense, penetrating eyes; magnetic and slightly mysterious quality",
        "meeting": "Through crisis, deep conversations, occult or psychological interests, or transformative circumstances",
        "challenges": "Jealousy and control issues; struggles with vulnerability",
    },
    "Sagittarius": {
        "personality": "Adventurous, philosophical, and freedom-loving",
        "traits": ["Broad-minded and open to diverse cultures", "Loves travel, learning, and expanding horizons", "Optimistic and enthusiastic life partner", "Values truth and directness above social polish"],
        "appearance": "Tall or well-proportioned; outdoor or athletic energy; open face",
        "meeting": "Through travel, higher education, spiritual retreats, or foreign connections",
        "challenges": "May avoid commitment or prioritise freedom over stability",
    },
    "Capricorn": {
        "personality": "Ambitious, disciplined, and deeply responsible",
        "traits": ["Takes relationships seriously and builds for the long term", "Practical and reliable provider", "Quietly affectionate — shows love through action", "Respects tradition, hard work, and achievement"],
        "appearance": "Distinguished bearing, strong bone structure, often looks better with age",
        "meeting": "Through professional settings, career events, or introductions via family",
        "challenges": "Can be emotionally reserved or prioritise career over intimacy",
    },
    "Aquarius": {
        "personality": "Original, humanitarian, and intellectually independent",
        "traits": ["Unique and unconventional in all the right ways", "Deeply committed to ideals and progressive values", "Friendly to everyone but emotionally selective", "Intellectual chemistry is the primary love language"],
        "appearance": "Distinctive personal style; often unusual or memorable features",
        "meeting": "Through activism, technology, groups, or unconventional circumstances",
        "challenges": "May be emotionally detached or prioritise ideas over intimacy",
    },
    "Pisces": {
        "personality": "Compassionate, intuitive, and deeply romantic",
        "traits": ["Empathic beyond ordinary human limits", "Artistic, spiritual, and emotionally fluid", "Selfless love — puts partner's needs first", "Connects on a soul level rather than just surface"],
        "appearance": "Dreamy eyes, gentle manner, ethereal or otherworldly quality",
        "meeting": "Through artistic, spiritual, or creative settings; or through a sense of destined connection",
        "challenges": "May lack practical grounding or struggle with boundaries",
    },
}

# Qualities indicated by Venus sign (natural significator of love)
VENUS_SIGN_LOVE = {
    "Aries":       "You love boldly and passionately — you are attracted to confidence, directness, and people who make the first move.",
    "Taurus":      "You love sensually and steadily — you seek security, physical affection, and beauty in a partner.",
    "Gemini":      "You love with your mind — wit, conversation, and intellectual chemistry are your deepest aphrodisiacs.",
    "Cancer":      "You love protectively and devotedly — emotional safety and a nurturing dynamic are what you need most.",
    "Leo":         "You love grandly and generously — you thrive with a partner who adores you and whom you can adore in return.",
    "Virgo":       "You love through service and attention to detail — you show care in thoughtful practical actions.",
    "Libra":       "You love harmoniously and aesthetically — beauty, fairness, and romantic idealism define your love language.",
    "Scorpio":     "You love with total intensity — you seek soul-deep merger and are unmoved by surface-level connection.",
    "Sagittarius": "You love freely and philosophically — adventure, honesty, and shared growth are your relationship foundation.",
    "Capricorn":   "You love with loyalty and long-term intention — you build love like a structure, slowly and to last.",
    "Aquarius":    "You love uniquely and intellectually — you need a partner who is also a genuine friend and free thinker.",
    "Pisces":      "You love unconditionally and spiritually — you merge deeply with a partner and seek transcendent connection.",
}

# What the 7th house lord in each house indicates about the partner/relationship
SEVENTH_LORD_IN_HOUSE = {
    1:  "Your partner is likely to be like you in many ways — similar values, similar energy, possibly similar background. The relationship is front and centre in your identity and self-expression.",
    2:  "Your partner contributes significantly to your wealth and family life. They may come from a prosperous background or be strongly family-oriented. Marriage is tied to financial growth.",
    3:  "Your partner may be communicative, artistic, or from a nearby location. You may meet through writing, media, or a sibling's introduction. The relationship is stimulating and requires good communication.",
    4:  "Your partner is homebody, emotionally nurturing, and deeply family-connected. The relationship brings stability, property, and a strong domestic life. May meet through family or home-related circumstances.",
    5:  "A romantic, creative, and intelligent partner is indicated. You may meet through creative pursuits, education, or a love affair that becomes a marriage. The relationship brings joy, children, and artistic growth.",
    6:  "The partner may be met through work, health settings, or service roles. There can be an element of service or sacrifice in the relationship. Choose your partner carefully and maintain clear boundaries.",
    7:  "A strong, powerful, and often physically attractive partner. The 7th lord in its own house gives a partner who is a true equal — decisive, independent, and relationship-focused.",
    8:  "A mysterious, intense, and transformative partner. The relationship itself becomes a vehicle for profound personal change. The partner may have hidden depth, unusual resources, or connection to occult/healing fields.",
    9:  "A partner with strong dharmic values — philosophical, spiritual, or from a foreign culture. The relationship expands your worldview and may involve travel or higher learning together.",
    10: "A partner with strong career ambitions and a public presence. You may meet through professional settings. The relationship boosts social status and career for both.",
    11: "A partner who begins as a friend or comes through your social network. The relationship fulfils long-held dreams and brings social connections. Financial gains through marriage are likely.",
    12: "A partner who may be foreign-born, spiritually inclined, or met through travel, retreat, or hospital settings. The relationship has a private, somewhat otherworldly quality. Deep soulmate potential.",
}


# ═══════════════════════════════════════════════════════════════════════════════
# ARUDHA LAGNA INTERPRETATIONS
# How the world perceives you — your public image and material reality
# ═══════════════════════════════════════════════════════════════════════════════

ARUDHA_INTERP = {
    "Aries": {
        "tagline": "The world sees a fearless pioneer.",
        "image": "You project boldness, confidence, and raw energy. People perceive you as a natural leader — decisive, action-oriented, and never afraid to go first. Your public persona radiates vitality and courage, and others look to you when swift action is needed.",
        "material": "Your material reality is built on initiative and competition. Wealth and recognition come through independent ventures, physical industries, real estate, or fields requiring courage. You tend to acquire resources quickly and impulsively.",
        "shadow": "Guard against being seen as reckless or aggressive. The world may also expect you to always be the strong one — a burden if your inner reality is more complex.",
        "keywords": ["Pioneer", "Fearless", "Action", "Vitality", "Leadership"],
    },
    "Taurus": {
        "tagline": "The world sees a pillar of stability and grace.",
        "image": "You project an aura of reliability, sensuality, and quiet strength. People perceive you as grounded, prosperous, and pleasurable to be around. Your public image often carries an aesthetic quality — others associate you with beauty, taste, and dependability.",
        "material": "Material life is rich and steady. Wealth accumulates through land, luxury goods, music, food, beauty industries, or anything that engages the senses. You build slowly but solidly — what you create lasts.",
        "shadow": "Others may perceive you as possessive, stubborn, or overly materialistic. The world may underestimate your intellectual depth because your physical presence is so commanding.",
        "keywords": ["Stability", "Beauty", "Wealth", "Sensuality", "Reliability"],
    },
    "Gemini": {
        "tagline": "The world sees a brilliant communicator and connector.",
        "image": "You project wit, versatility, and intellectual curiosity. People perceive you as quick-minded, sociable, and always interesting — someone who knows a little about everything and connects ideas effortlessly. Your public image is youthful and engaging.",
        "material": "Material life flows through communication, media, trade, writing, teaching, or networks. Multiple income streams are common. Your material world is dynamic and changeable — you thrive on variety rather than rigid structures.",
        "shadow": "Others may see you as scattered, superficial, or inconsistent. Your quick-shifting persona can make you hard to pin down — which may undermine trust in professional settings.",
        "keywords": ["Intelligence", "Communication", "Versatility", "Networks", "Wit"],
    },
    "Cancer": {
        "tagline": "The world sees a nurturing protector with deep roots.",
        "image": "You project warmth, emotional depth, and a sense of home wherever you go. People perceive you as caring, intuitive, and deeply connected to family and tradition. Your public presence feels maternal, protective, and emotionally safe.",
        "material": "Material life is tied to land, property, food, family wealth, or ancestral inheritance. Emotional security and financial security are deeply linked for you. Home ownership and nurturing others often become financial pillars.",
        "shadow": "Others may see you as overly emotional, clingy, or resistant to change. The world may project its need for comfort onto you — expecting more care than you can give.",
        "keywords": ["Nurturing", "Intuition", "Home", "Ancestry", "Emotional depth"],
    },
    "Leo": {
        "tagline": "The world sees royalty — a bright, magnetic sovereign.",
        "image": "You project authority, charisma, and creative power. People see you as larger than life — dramatic, generous, and radiantly self-assured. Your public image commands attention naturally; rooms change when you enter.",
        "material": "Material life is connected to fame, leadership, entertainment, government, gold, luxury, and creative self-expression. Status and recognition are as important as money. You spend lavishly and attract resources through your personal brand.",
        "shadow": "The world may perceive you as arrogant, domineering, or attention-seeking. Living up to the royal image can become exhausting — especially when your inner self craves privacy.",
        "keywords": ["Royalty", "Fame", "Creativity", "Authority", "Charisma"],
    },
    "Virgo": {
        "tagline": "The world sees a precise, capable, and selfless craftsperson.",
        "image": "You project competence, discernment, and methodical intelligence. People see you as hardworking, analytical, and deeply service-oriented. Your public image is one of the reliable expert — the person who gets things right.",
        "material": "Wealth comes through skilled service, health, healing, accounting, technology, writing, or craftsmanship. Material life rewards precision and dedication. You are often paid for your expertise rather than your personality.",
        "shadow": "Others may see you as critical, anxious, or overly modest. Your drive for perfection can lead the world to demand impossible standards from you.",
        "keywords": ["Service", "Precision", "Craft", "Health", "Intelligence"],
    },
    "Libra": {
        "tagline": "The world sees a charming diplomat wrapped in elegance.",
        "image": "You project grace, fairness, and social harmony. People perceive you as cultured, balanced, and naturally attractive — someone who brings beauty and resolution wherever you go. Partnerships and collaborations define your public face.",
        "material": "Material life flourishes through partnerships, law, luxury, fashion, diplomacy, arts, or media. Wealth often comes through others — via marriage, joint ventures, or influential allies. Your material world is built on relationships.",
        "shadow": "Others may see you as indecisive, approval-seeking, or superficial. The expectation of being always balanced and fair can mask your own needs.",
        "keywords": ["Harmony", "Elegance", "Diplomacy", "Partnership", "Justice"],
    },
    "Scorpio": {
        "tagline": "The world sees a powerful, magnetic force of transformation.",
        "image": "You project intensity, depth, and an air of mystery. People perceive you as formidable — someone with hidden knowledge, iron will, and transformative power. Your public image is magnetic and slightly dangerous, drawing others in even as it unsettles them.",
        "material": "Material life involves other people's resources — inheritance, insurance, investment, research, psychology, occult sciences, or crisis management. Wealth often comes from transformation and deep investigation.",
        "shadow": "Others may perceive you as controlling, secretive, or ruthless. The world projects its fears and desires onto you — making your public image a powerful but double-edged sword.",
        "keywords": ["Power", "Transformation", "Depth", "Mystery", "Intensity"],
    },
    "Sagittarius": {
        "tagline": "The world sees a wise philosopher and free-spirited adventurer.",
        "image": "You project optimism, wisdom, and boundless enthusiasm. People see you as a teacher, explorer, or visionary — someone who expands horizons and inspires others toward higher meaning. Your public image is warm, philosophical, and larger-than-life.",
        "material": "Wealth and recognition come through higher education, publishing, travel, law, religion, philosophy, or international affairs. Your material life is expansive and often linked to foreign lands or big ideas.",
        "shadow": "Others may see you as preachy, overextended, or unrealistic. The world expects you to be perpetually positive — which may mask genuine doubts or struggles.",
        "keywords": ["Wisdom", "Adventure", "Philosophy", "Freedom", "Expansion"],
    },
    "Capricorn": {
        "tagline": "The world sees a disciplined architect of lasting achievement.",
        "image": "You project ambition, authority, and quiet determination. People perceive you as serious, capable, and responsible — someone who builds slowly but leaves an enduring legacy. Your public image grows more impressive with age.",
        "material": "Material life is substantial and earned through discipline, government, corporate leadership, real estate, engineering, or long-term investment. Wealth accumulates steadily over decades. Status and security are paramount.",
        "shadow": "Others may see you as cold, rigid, or overly status-conscious. The world may project its need for authority onto you — burdening you with responsibilities you did not seek.",
        "keywords": ["Ambition", "Discipline", "Legacy", "Authority", "Structure"],
    },
    "Aquarius": {
        "tagline": "The world sees a visionary innovator ahead of their time.",
        "image": "You project originality, independence, and humanitarian idealism. People see you as unconventional, intellectually formidable, and committed to collective progress. Your public image is that of the revolutionary mind — the one who changes systems.",
        "material": "Material life comes through technology, social reform, science, community networks, or cutting-edge innovation. Wealth is often unpredictable — arriving in sudden, surprising ways. Your value to the world is in your ideas.",
        "shadow": "Others may see you as detached, eccentric, or contrarian. The world may expect you to be the rebel forever — even when you crave stability and belonging.",
        "keywords": ["Innovation", "Independence", "Humanity", "Vision", "Revolution"],
    },
    "Pisces": {
        "tagline": "The world sees a compassionate mystic flowing between worlds.",
        "image": "You project sensitivity, creativity, and spiritual depth. People perceive you as ethereal, empathetic, and somehow otherworldly — a dreamer who touches the unseen. Your public image is soft, artistic, and deeply feeling.",
        "material": "Material life is fluid and non-linear — wealth arrives through artistic creation, spiritual work, healing, film, poetry, or ocean-related industries. Financial life can be abundant but also diffuse; discipline is needed to anchor resources.",
        "shadow": "Others may see you as elusive, unreliable, or impractical. The world may project its need for escape and transcendence onto you — making boundaries essential.",
        "keywords": ["Compassion", "Creativity", "Spirituality", "Dreams", "Healing"],
    },
}


# ═══════════════════════════════════════════════════════════════════════════════
# INDU LAGNA INTERPRETATIONS
# The prosperity lagna — wealth potential, financial dharma, abundance themes
# ═══════════════════════════════════════════════════════════════════════════════

INDU_INTERP = {
    "Aries": {
        "tagline": "Wealth through bold action and independent enterprise.",
        "description": "Your Indu Lagna in Aries points to a wealth potential that is activated by initiative, courage, and entrepreneurship. You are destined to create wealth rather than inherit it — financial abundance arrives when you act first and think second. The pioneering spirit is your greatest asset.",
        "sources": ["Entrepreneurship", "Competitive industries", "Real estate", "Sports & physical trades", "Military or security fields"],
        "timing": "Wealth surges during Mars dasha periods and when Mars transits your Indu Lagna. Action taken during Aries-activated periods brings financial breakthroughs.",
        "advice": "Stop waiting for the right moment. Your Indu Lagna demands decisiveness — the window of wealth opens when you move.",
    },
    "Taurus": {
        "tagline": "Wealth through beauty, patience, and accumulation.",
        "description": "Indu Lagna in Taurus is one of the most auspicious wealth placements. Venus, the natural significator of material abundance, rules this sign — indicating that your financial destiny is rich, sensual, and enduring. Wealth builds slowly but becomes deeply solid.",
        "sources": ["Land and property", "Luxury goods", "Music and arts", "Finance and banking", "Food and agriculture", "Beauty industries"],
        "timing": "Venus dasha and sub-periods are peak wealth-building times. Jupiter and Moon transits over Taurus further activate prosperity.",
        "advice": "Invest in tangibles — land, art, high-quality assets. Patience is your superpower; compounding wealth over time is your dharma.",
    },
    "Gemini": {
        "tagline": "Wealth through communication, commerce, and networks.",
        "description": "Indu Lagna in Gemini indicates that your financial dharma runs through words, information, and connections. You are built to profit from ideas, media, trade, and intellectual exchanges. Multiple income streams are natural — variety is your wealth strategy.",
        "sources": ["Media and publishing", "Teaching and training", "Sales and commerce", "Technology and software", "Writing and journalism"],
        "timing": "Mercury dasha and sub-periods activate your prosperity. Rahu can amplify financial gains through unconventional intellectual paths.",
        "advice": "Network deliberately. Your wealth is often one conversation or one connection away. Leverage multiple income streams simultaneously.",
    },
    "Cancer": {
        "tagline": "Wealth through land, nurturing, and ancestral blessings.",
        "description": "Indu Lagna in Cancer places your wealth potential deep in the emotional, familial, and ancestral realm. The Moon rules Cancer — and wherever the Moon flows, abundance follows for you. Property, family enterprises, and care-based industries are your financial heartland.",
        "sources": ["Real estate and land", "Food and hospitality", "Family businesses", "Childcare and education", "Psychology and healing"],
        "timing": "Moon dasha and Cancer-activated periods bring financial nourishment. Full Moons transiting Cancer can trigger income surges.",
        "advice": "Invest in property and family assets. Your ancestral blessings are a real financial force — honor them and they multiply.",
    },
    "Leo": {
        "tagline": "Wealth through leadership, creativity, and public recognition.",
        "description": "Indu Lagna in Leo is a royal wealth signature. The Sun governs this sign, and your prosperity is tied to personal authority, creative genius, and public standing. The more you shine your authentic self, the more abundance flows — wealth follows your light.",
        "sources": ["Entertainment and performance", "Government and leadership", "Gold and precious metals", "Creative industries", "Corporate management"],
        "timing": "Sun dasha and Leo-active periods bring peak financial recognition. Jupiter transiting Leo amplifies prosperity significantly.",
        "advice": "Build your personal brand fearlessly. Your reputation is your balance sheet — invest in visibility, confidence, and creative excellence.",
    },
    "Virgo": {
        "tagline": "Wealth through mastery, service, and meticulous skill.",
        "description": "Indu Lagna in Virgo indicates that your financial destiny is built on expertise, precision, and service to others. Mercury governs Virgo, and your wealth arrives through intellectual mastery and practical skill. The more refined your craft, the richer your life becomes.",
        "sources": ["Healthcare and healing", "Accounting and analysis", "Technology and engineering", "Agriculture and nutrition", "Publishing and editing"],
        "timing": "Mercury dasha periods are key wealth-building phases. Transits of Jupiter through Virgo bring expansion of material life.",
        "advice": "Invest in your skills continuously. Financial abundance is the natural reward for becoming world-class at what you do.",
    },
    "Libra": {
        "tagline": "Wealth through partnerships, beauty, and balanced exchange.",
        "description": "Indu Lagna in Libra points to prosperity arriving through relationships, joint ventures, and the creation of beauty and harmony. Venus rules Libra — and your financial dharma is social, aesthetic, and collaborative. Your wealthiest moments come when you partner wisely.",
        "sources": ["Legal profession", "Fashion and design", "Luxury and lifestyle", "Partnership ventures", "Diplomacy and counseling"],
        "timing": "Venus dasha periods are your most prosperous phases. Jupiter transiting Libra brings financial blessings through partnerships.",
        "advice": "Choose partners with extreme care — they are financial amplifiers or drains. Invest in your aesthetic environment as it literally attracts abundance.",
    },
    "Scorpio": {
        "tagline": "Wealth through transformation, research, and other people's resources.",
        "description": "Indu Lagna in Scorpio is one of the most powerful wealth indicators for dealing with deep resources — inheritance, investment, insurance, joint finances, and occult knowledge. Mars and Ketu govern Scorpio; your wealth arrives through going where others fear to tread.",
        "sources": ["Investment banking and finance", "Research and investigation", "Inheritance and estate management", "Psychology and therapy", "Mining and hidden resources"],
        "timing": "Mars and Ketu dasha periods trigger financial transformation. Intense periods often precede the greatest wealth surges.",
        "advice": "Study finance and investment deeply — this is your natural domain. Don't shy away from complex financial structures; they are your wealth playground.",
    },
    "Sagittarius": {
        "tagline": "Wealth through wisdom, travel, and the expansion of horizons.",
        "description": "Indu Lagna in Sagittarius gives a broad, expansive, and optimistic financial destiny. Jupiter rules Sagittarius — and the great benefic blesses this position abundantly. Your wealth is tied to wisdom, higher education, travel, and the transmission of knowledge.",
        "sources": ["Higher education and academia", "Publishing and philosophy", "International trade", "Law and justice", "Spiritual teaching and guidance"],
        "timing": "Jupiter dasha is your peak wealth period. Transits of Jupiter through Sagittarius bring major prosperity expansion.",
        "advice": "Think globally and invest in education — yours and others'. Your generosity and philosophical vision are not costs; they are wealth generators.",
    },
    "Capricorn": {
        "tagline": "Wealth through discipline, structure, and long-term mastery.",
        "description": "Indu Lagna in Capricorn is a wealth signature of patient, disciplined accumulation. Saturn rules this sign, and while wealth may come slowly, it comes with extraordinary permanence and scale. You are built for generational wealth.",
        "sources": ["Corporate leadership", "Real estate development", "Government and administration", "Engineering and construction", "Long-term investments"],
        "timing": "Saturn dasha is your most productive wealth-building period. Slow, steady progress during Saturn years creates unshakeable financial foundations.",
        "advice": "Play the long game — always. Every financial decision should serve a 10-year vision. Compound time is your greatest ally.",
    },
    "Aquarius": {
        "tagline": "Wealth through innovation, networks, and visionary ideas.",
        "description": "Indu Lagna in Aquarius points to financial destiny tied to technology, social networks, and revolutionary ideas. Saturn and Rahu co-govern Aquarius — wealth arrives through unconventional paths, digital innovation, or serving large communities.",
        "sources": ["Technology and startups", "Social media and digital platforms", "Scientific research", "Community enterprises", "Astrology and metaphysical sciences"],
        "timing": "Saturn and Rahu dasha periods bring unexpected financial opportunities. Jupiter transiting Aquarius opens doors in social and technological domains.",
        "advice": "Build networks and platforms over individual relationships. One scalable system can generate more wealth than a thousand individual transactions.",
    },
    "Pisces": {
        "tagline": "Wealth through creativity, spirituality, and compassionate service.",
        "description": "Indu Lagna in Pisces places your financial dharma in the realm of dreams, healing, art, and spiritual service. Jupiter co-rules Pisces, bestowing natural grace around abundance — but only when you align work with soul purpose. Your wealth is spiritual in origin.",
        "sources": ["Artistic and creative work", "Spiritual teaching and healing", "Film, music, and poetry", "Medical and pharmaceutical fields", "Charity and non-profit leadership"],
        "timing": "Jupiter and Ketu dasha periods bring spiritual wealth and material abundance together. Neptune-like periods of dissolution often precede major financial renewal.",
        "advice": "Trust that your spiritual alignment IS your wealth strategy. When you serve from the soul, the material follows. Avoid sacrificing purpose for security.",
    },
}


def get_arudha_interpretation(sign):
    return ARUDHA_INTERP.get(sign, {})

def get_indu_interpretation(sign):
    return INDU_INTERP.get(sign, {})
