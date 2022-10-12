"""
Usually when you buy something, you're asked whether your credit card number, phone number or answer to your most secret question is still correct. However, since someone could look over your shoulder, you don't want that shown on your screen. Instead, we mask it.
Your task is to write a function maskify, which changes all but the last four characters into '#'.

Examples:

"4556364607935616" --> "############5616"
     "64607935616" -->      "#######5616"
               "1" -->                "1"
                "" -->                 ""

// "What was the name of your first pet?"

"Skippy" --> "##ippy"
"""

def maskify(cc):
    """
    Returns masked string
    """
    last_four = cc[len(cc) - 4:]
    if len(last_four) >= 4:
        new_cc = "#" * (len(cc) - 4) + last_four 
        return new_cc
    else:
        return cc

# maskify("xxxxxxxxxxxxxxxx!5555")
# maskify("4556364607935616")
# maskify("64607935616")
# maskify("1")
# maskify("")
# maskify("Skippy")
# maskify('123')
# maskify('SF$SDfgsd2eA')
# maskify('4444')

