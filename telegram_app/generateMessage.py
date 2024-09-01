def generate_message(data):
    dexSocialLink, twitterLink, tokenCA, chain, tokenName, tokenSymbol, telegram, twitter, website = data

    required_fields = [dexSocialLink, twitterLink, tokenCA, chain, tokenName, tokenSymbol]
    if any(field is None or field == "" or field == "NA" for field in required_fields):
        return None

    message = f"""
[📣](emoji/5424818078833715060) DexSocials - Recently Updated Listing -  [🪙](emoji/5289516520131535412){chain}

[💎](emoji/5427168083074628963)Token: [{tokenName} ({tokenSymbol})](https://dexsocials.com/{chain.lower()}/{tokenCA})

[📄](emoji/5377705435807619775) Contract: `{tokenCA}`

[🔥](emoji/5424972470023104089){tokenName} Socials

"""

    # Add optional fields if they are provided and not "NA"
    if telegram and telegram != "NA":
        message += f"[✈️](emoji/5278689083671978389)Telegram: [@{telegram}](https://t.me/{telegram})\n"
    if twitter and twitter != "NA":
        message += f"[✖️](emoji/5420151592571646424)X: [@{twitter}](https://x.com/{twitter})\n"
    if website and website != "NA":
        message += f"🌐 Website: [{website}](http://{website}/)\n"

    message += """____________________________
[📱](emoji/5330337435500951363) [Boost On X](https://x.com/dexsocialscom/status/1826238461801824312)

[📱](emoji/5330237710655306682) [Updated listings](https://t.me/dexsocialsupdates)  | [📱](emoji/5359758030198031389) [Dexsocials.com](https://dexsocials.com/)
"""
    return message
