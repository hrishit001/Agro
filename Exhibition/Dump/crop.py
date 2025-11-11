from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.lib import colors

pdf_path = "Rice_Cultivation_Guide.pdf"

doc = SimpleDocTemplate(pdf_path, pagesize=A4)
styles = getSampleStyleSheet()

title_style = ParagraphStyle(
    name="Title",
    fontSize=20,
    leading=24,
    alignment=TA_CENTER,
    textColor=colors.green,
    spaceAfter=20
)
sub_style = ParagraphStyle(
    name="SubTitle",
    fontSize=14,
    leading=18,
    textColor=colors.darkgreen,
    spaceAfter=10
)
body_style = ParagraphStyle(
    name="Body",
    fontSize=11,
    leading=16,
    spaceAfter=10
)

story = []

# Title
story.append(Paragraph("Rice (धान) Cultivation Guide", title_style))
story.append(Spacer(1, 12))



# English Section
story.append(Paragraph("<b>Crop Name:</b> Rice (धान)", sub_style))
story.append(Paragraph("Scientific Name: Oryza sativa", body_style))
story.append(Paragraph("Major Growing States: West Bengal, Punjab, Uttar Pradesh, Bihar, Tamil Nadu, Andhra Pradesh, Chhattisgarh", body_style))
story.append(Paragraph("<b>Ideal Climate and Soil</b>", sub_style))
story.append(Paragraph("Temperature: 20°C – 37°C<br/>Rainfall: 1000 – 2000 mm<br/>Humidity: 60% – 85%<br/>Soil: Fertile clayey or loamy soil with good water retention", body_style))
story.append(Paragraph("NPK Ratio (kg/ha): N: 100–150, P: 50–70, K: 50–60", body_style))
story.append(Paragraph("<b>Growth Stages:</b> Germination, Transplanting, Tillering, Flowering, Maturity", body_style))
story.append(Paragraph("<b>Care:</b> Maintain 5–10 cm water, apply fertilizers in 3 splits, control weeds.", body_style))
story.append(Paragraph("<b>Common Varieties:</b> IR-36, Swarna, Pusa Basmati-1, Jaya, PR-106, IR-64", body_style))
story.append(Paragraph("<b>Pests:</b> Stem borer, Leaf blast, Brown plant hopper", body_style))
story.append(Paragraph("<b>Harvest:</b> 80–85% grains mature, yield 4–6 tonnes/ha.", body_style))
story.append(Spacer(1, 12))

# Hindi Section
story.append(Paragraph("<b>धान की खेती मार्गदर्शिका</b>", title_style))
story.append(Paragraph("वैज्ञानिक नाम: Oryza sativa", body_style))
story.append(Paragraph("मुख्य राज्य: पश्चिम बंगाल, पंजाब, उत्तर प्रदेश, बिहार, तमिलनाडु, आंध्र प्रदेश, छत्तीसगढ़", body_style))
story.append(Paragraph("<b>उपयुक्त जलवायु और मिट्टी</b>", sub_style))
story.append(Paragraph("तापमान: 20°C – 37°C<br/>वर्षा: 1000 – 2000 मिमी<br/>आर्द्रता: 60% – 85%<br/>मिट्टी: उपजाऊ दोमट या चिकनी मिट्टी जो पानी रोक सके", body_style))
story.append(Paragraph("NPK अनुपात (किग्रा/हे.): N: 100–150, P: 50–70, K: 50–60", body_style))
story.append(Paragraph("<b>वृद्धि चरण:</b> अंकुरण, रोपाई, टिलरिंग, फूल लगना, पकना", body_style))
story.append(Paragraph("<b>देखभाल:</b> 5–10 सेमी पानी बनाए रखें, यूरिया तीन बार डालें, खरपतवार नियंत्रण करें।", body_style))
story.append(Paragraph("<b>प्रमुख किस्में:</b> IR-36, स्वर्ण, पूसा बासमती-1, जया, PR-106, IR-64", body_style))
story.append(Paragraph("<b>रोग:</b> स्टेम बोरर, लीफ ब्लास्ट, ब्राउन प्लांट हॉपर", body_style))
story.append(Paragraph("<b>कटाई:</b> जब 80–85% दाने पक जाएं, औसत उत्पादन 4–6 टन/हेक्टेयर।", body_style))

doc.build(story)
print("✅ PDF created successfully:", pdf_path)
