text = "X-DSPAM-Confidence:    0.8475"
colon = text.find(':')
extract = text[colon+2:]
as_num = float(extract)
print(as_num)
