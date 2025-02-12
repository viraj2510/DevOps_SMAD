const colorInput = document.getElementById("colorInput");
const output = document.getElementById("output");

colorInput.addEventListener("input", function () {
    let hexColor = colorInput.value;
    let rgbColor = hexToRgb(hexColor);
    document.body.style.backgroundColor = hexColor;
    output.innerHTML = `HEX: ${hexColor} | RGB: ${rgbColor}`;
});

function hexToRgb(hex) {
    let r = parseInt(hex.slice(1, 3), 16);
    let g = parseInt(hex.slice(3, 5), 16);
    let b = parseInt(hex.slice(5, 7), 16);
    return `(${r}, ${g}, ${b})`;
}
