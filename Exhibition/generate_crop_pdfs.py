from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle, Spacer

# PDF setup
pdf = SimpleDocTemplate("Sugarcane_Cultivation_Guide.pdf", pagesize=A4,
                        rightMargin=40, leftMargin=40, topMargin=40, bottomMargin=40)

styles = getSampleStyleSheet()
style_title = ParagraphStyle('title', parent=styles['Heading1'], alignment=1, spaceAfter=14, fontSize=18, textColor=colors.HexColor("#2E7D32"))
style_heading = ParagraphStyle('heading', parent=styles['Heading2'], spaceBefore=10, spaceAfter=6, textColor=colors.HexColor("#1B5E20"), fontSize=13)
style_normal = ParagraphStyle('normal', parent=styles['Normal'], fontSize=10, leading=14)

elements = []

# Title
elements.append(Paragraph("Sugarcane Cultivation Guide", style_title))
elements.append(Paragraph(
    "Sugarcane (<i>Saccharum officinarum</i>) is a major tropical and subtropical crop extensively grown in India for sugar production, biofuel, and various industrial products.",
    style_normal))

# Section: Growth Requirements
elements.append(Spacer(1, 8))
elements.append(Paragraph("Growth Requirements", style_heading))

data1 = [
    ["Requirement", "Optimal Range", "Notes"],
    ["Temperature", "20–35°C", "Warm temperature range essential for germination and growth."],
    ["Rainfall", "750–1200 mm annually", "Evenly distributed rainfall preferred; irrigation supplements in dry areas."],
    ["Soil", "Deep loamy, well-drained", "pH 6.5–7.5 ideal; fertile soil rich in organic matter promotes productivity."],
    ["Crop duration", "10–18 months", "Duration depends on region and variety, commonly about 12 months."]
]

table1 = Table(data1, colWidths=[100, 130, 250])
table1.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#A5D6A7")),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('BACKGROUND', (0, 1), (-1, -1), colors.whitesmoke),
    ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.whitesmoke, colors.HexColor("#E8F5E9")]),
    ('FONTSIZE', (0, 0), (-1, -1), 9),
    ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ('BOX', (0, 0), (-1, -1), 0.6, colors.HexColor("#2E7D32")),
    ('INNERGRID', (0, 0), (-1, -1), 0.4, colors.grey)
]))
elements.append(table1)

# Section: Fertilization
elements.append(Spacer(1, 10))
elements.append(Paragraph("Recommended NPK Fertilization (kg/ha)", style_heading))

data2 = [
    ["Nutrient", "Recommended Dosage", "Purpose"],
    ["Nitrogen (N)", "100–180", "Promotes vegetative growth and sucrose accumulation."],
    ["Phosphorus (P)", "40–60", "Enhances root development and early growth."],
    ["Potassium (K)", "150–200", "Raises sugar content, stress tolerance, and overall vigor."]
]

table2 = Table(data2, colWidths=[110, 120, 250])
table2.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#A5D6A7")),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('BACKGROUND', (0, 1), (-1, -1), colors.HexColor("#F1F8E9")),
    ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.whitesmoke, colors.HexColor("#E8F5E9")]),
    ('FONTSIZE', (0, 0), (-1, -1), 9),
    ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ('BOX', (0, 0), (-1, -1), 0.6, colors.HexColor("#2E7D32")),
    ('INNERGRID', (0, 0), (-1, -1), 0.4, colors.grey)
]))
elements.append(table2)

elements.append(Spacer(1, 6))
elements.append(Paragraph(
    "<b>Application Schedule:</b><br/>• Basal application of phosphorus and potassium before planting.<br/>"
    "• Nitrogen applied in split doses during growth stages to maximize uptake.",
    style_normal))

# Section: Best Cultivation Practices
elements.append(Spacer(1, 10))
elements.append(Paragraph("Best Cultivation Practices", style_heading))
elements.append(Paragraph(
    "• <b>Seed Treatment:</b> Soak setts for 6–8 hours; apply fungicides to protect from diseases.<br/>"
    "• <b>Land Preparation:</b> Deep ploughing followed by leveling and bed preparation with raised beds about 120 cm wide.<br/>"
    "• <b>Planting Methods:</b> Includes flat, furrow, trench, and distant planting tailored to soil and water conditions.<br/>"
    "• <b>Irrigation:</b> Requires regular irrigation during growth; flood irrigation or drip irrigation for water saving.<br/>"
    "• <b>Weed and Pest Management:</b> Regular intercultural operations and integrated pest management to control pests and weeds.<br/>"
    "• <b>Crop Rotation:</b> Follow with legumes or cereals to maintain soil fertility and health.",
    style_normal))

# Section: Harvesting and Post-Harvest
elements.append(Spacer(1, 10))
elements.append(Paragraph("Harvesting and Post-Harvest", style_heading))
elements.append(Paragraph(
    "• Typically harvested 10–18 months after planting based on maturity and sugar content.<br/>"
    "• Manual harvesting predominates; mechanization is increasing in some regions.<br/>"
    "• Post-harvest involves careful handling, cleaning, and timely transport to processing units to minimize losses.",
    style_normal))



# Build PDF
pdf.build(elements)
print("✅ Sugarcane_Cultivation_Guide.pdf generated successfully with colorful layout!")
