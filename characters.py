"""Character archetype matching based on sidereal birth chart."""

SIGN_CHARACTERS = {
    "Aries": {
        "mbti": "ESTP",
        "mbti_desc": "Bold, action-first, thrives under pressure — the Dynamo",
        "naruto":      {"M": "Naruto Uzumaki",     "F": "Sakura Haruno"},
        "one_piece":   {"M": "Monkey D. Luffy",    "F": "Nami"},
        "mahabharata": {"M": "Bhima",               "F": "Draupadi"},
        "ramayana":    {"M": "Hanuman",             "F": "Sita"},
    },
    "Taurus": {
        "mbti": "ISFJ",
        "mbti_desc": "Steadfast, loyal, grounded in comfort and security — the Defender",
        "naruto":      {"M": "Rock Lee",            "F": "Tsunade"},
        "one_piece":   {"M": "Roronoa Zoro",        "F": "Nami"},
        "mahabharata": {"M": "Bhishma",             "F": "Kunti"},
        "ramayana":    {"M": "Rama",                "F": "Sita"},
    },
    "Gemini": {
        "mbti": "ENTP",
        "mbti_desc": "Curious, quick-witted, loves ideas and debate — the Visionary",
        "naruto":      {"M": "Kakashi Hatake",      "F": "Ino Yamanaka"},
        "one_piece":   {"M": "Usopp",               "F": "Nami"},
        "mahabharata": {"M": "Sahadeva",            "F": "Subhadra"},
        "ramayana":    {"M": "Lakshmana",           "F": "Shurpanakha"},
    },
    "Cancer": {
        "mbti": "INFJ",
        "mbti_desc": "Deeply empathetic, intuitive, fiercely protective — the Advocate",
        "naruto":      {"M": "Shino Aburame",       "F": "Hinata Hyuga"},
        "one_piece":   {"M": "Tony Tony Chopper",   "F": "Nami"},
        "mahabharata": {"M": "Yudhishthira",        "F": "Gandhari"},
        "ramayana":    {"M": "Bharata",             "F": "Kausalya"},
    },
    "Leo": {
        "mbti": "ENFJ",
        "mbti_desc": "Charismatic, inspiring, a natural-born leader — the Protagonist",
        "naruto":      {"M": "Sasuke Uchiha",       "F": "Temari"},
        "one_piece":   {"M": "Portgas D. Ace",      "F": "Boa Hancock"},
        "mahabharata": {"M": "Karna",               "F": "Draupadi"},
        "ramayana":    {"M": "Rama",                "F": "Kaikeyi"},
    },
    "Virgo": {
        "mbti": "ISTJ",
        "mbti_desc": "Analytical, meticulous, deeply reliable — the Logistician",
        "naruto":      {"M": "Shikamaru Nara",      "F": "Ino Yamanaka"},
        "one_piece":   {"M": "Roronoa Zoro",        "F": "Nico Robin"},
        "mahabharata": {"M": "Drona",               "F": "Satyavati"},
        "ramayana":    {"M": "Bharata",             "F": "Sita"},
    },
    "Libra": {
        "mbti": "ESFJ",
        "mbti_desc": "Diplomatic, warm, seeks harmony in all things — the Consul",
        "naruto":      {"M": "Iruka Umino",         "F": "Kurenai Yuhi"},
        "one_piece":   {"M": "Sanji",               "F": "Nami"},
        "mahabharata": {"M": "Krishna",             "F": "Draupadi"},
        "ramayana":    {"M": "Lakshmana",           "F": "Mandodari"},
    },
    "Scorpio": {
        "mbti": "INTJ",
        "mbti_desc": "Intense, strategic, sees beneath every surface — the Architect",
        "naruto":      {"M": "Itachi Uchiha",       "F": "Anko Mitarashi"},
        "one_piece":   {"M": "Trafalgar D. Law",    "F": "Nico Robin"},
        "mahabharata": {"M": "Duryodhana",          "F": "Amba"},
        "ramayana":    {"M": "Ravana",              "F": "Kaikeyi"},
    },
    "Sagittarius": {
        "mbti": "ENFP",
        "mbti_desc": "Free-spirited, adventurous, endlessly optimistic — the Campaigner",
        "naruto":      {"M": "Jiraiya",             "F": "Tsunade"},
        "one_piece":   {"M": "Shanks",              "F": "Boa Hancock"},
        "mahabharata": {"M": "Arjuna",              "F": "Chitrangada"},
        "ramayana":    {"M": "Hanuman",             "F": "Tara"},
    },
    "Capricorn": {
        "mbti": "ENTJ",
        "mbti_desc": "Ambitious, disciplined, relentless drive toward mastery — the Commander",
        "naruto":      {"M": "Neji Hyuga",          "F": "Shizune"},
        "one_piece":   {"M": "Dracule Mihawk",      "F": "Nico Robin"},
        "mahabharata": {"M": "Yudhishthira",        "F": "Kunti"},
        "ramayana":    {"M": "Dasharatha",          "F": "Kausalya"},
    },
    "Aquarius": {
        "mbti": "INTP",
        "mbti_desc": "Visionary, unconventional, driven by pure curiosity — the Logician",
        "naruto":      {"M": "Orochimaru",          "F": "Konan"},
        "one_piece":   {"M": "Trafalgar D. Law",    "F": "Nico Robin"},
        "mahabharata": {"M": "Vidura",              "F": "Amba"},
        "ramayana":    {"M": "Vibhishana",          "F": "Mandodari"},
    },
    "Pisces": {
        "mbti": "INFP",
        "mbti_desc": "Deeply imaginative, empathetic, spiritually attuned — the Mediator",
        "naruto":      {"M": "Gaara",               "F": "Hinata Hyuga"},
        "one_piece":   {"M": "Tony Tony Chopper",   "F": "Princess Vivi"},
        "mahabharata": {"M": "Bhishma",             "F": "Gandhari"},
        "ramayana":    {"M": "Valmiki",             "F": "Sita"},
    },
}


def get_characters(sun_sign, moon_sign, rising_sign, gender="M"):
    """
    Return character archetypes for a given sidereal birth chart.
    Primary: sun sign. Gender selects the male/female character variant.
    """
    gender_key = "F" if (gender or "M").upper().startswith("F") else "M"
    data = SIGN_CHARACTERS.get(sun_sign, SIGN_CHARACTERS["Aries"])

    return {
        "mbti":        data["mbti"],
        "mbti_desc":   data["mbti_desc"],
        "naruto":      data["naruto"][gender_key],
        "one_piece":   data["one_piece"][gender_key],
        "mahabharata": data["mahabharata"][gender_key],
        "ramayana":    data["ramayana"][gender_key],
    }
