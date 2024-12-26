// ring number
Ring_number = 0;// [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

all_texts = [
  "●",
  "АВДЕЁЖЗИЙКЛМНОПРСТУХЧШЩЫЬЯ",
  "АБВДЕЁЖИЙКЛНОПРСТУФЦШЩЬЭЮЯ",
  "АБВГДЕЗИЙКЛМНОПРСТУХЧШЫЬЮЯ",
  "АБВГДЕЖИЙКЛНОПРСТУЧЩЪЫЬЭЮЯ",
  "АВГДЕЖИЙКЛМНОПРСТУХЦЧШЩЬЮЯ",
  "АВГДЕЗИЙКЛНОПРСТУХЦЧШЩЪЬЮЯ",
  "АВГДЕЁЖИЙКЛНОПРСТУФЦЧЩЪЫЬЯ",
  "АВГДЕЁЖИЙКЛМНОПРСТУФХЦЩЪЫЬ",
  "АБВДЕЁЖЗИЙКЛМНОПРСТУЦЧШЪЬЮ",
  "АВДЕЖИЙКЛМНОПРСТУФЦЧЩЫЬЭЮЯ"
];

// Parameters
ring_diameter = 75;// Diameter of the ring

text = all_texts[Ring_number];// String of letters to deboss
font_size = 6;// Font size for letters
font_style = "Liberation Sans Narrow:style=Bold";// Font style
letter_spacing = 360 / len(text);// Angular spacing between letters

module deboss_letter(letter, angle) {
  rotate([0, 0, 90 + angle])// Rotate around the ring
    translate([ring_diameter / 2, 0, 0])// Position on circumference
      rotate([90, -90, 90])
        linear_extrude(height = 2, center = true)// Extrude the text for debossing
          text(letter, size = font_size, font = font_style, halign = "center", valign = "center");
}

module debossed_ring() {
  for(i = [0:len(text) - 1])// Loop over all letters
    deboss_letter(text[i], i * letter_spacing);// Deboss each letter
}


difference() {

  translate([-87.5 - 75 / 2, -105, 0])
    import("Letter Ring (Blank).stl");
  // Render the debossed ring
  translate([0, 0, 4.5])
    debossed_ring();
}

