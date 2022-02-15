//retrieve node in DOM via ID
var c = document.getElementById("slate")

//instantiate a CanvasRenderingContext2D Object
var ctx = c.getContext("2d");

//intit global state var
var mode = "rect";

//var toggleMode = function(e) {
var toggleMode = function(e) {
    console.log("toggling...")
    if (mode == "rect") {
      mode = "circle";
    }
    else {
      mode = "rect";
    }
}

var drawRect = function(e) {
    var mouseX = e.offsetX;
    var mouseY = e.offsetY;
    ctx.beginPath()
    ctx.rect(mouseX, mouseY, 100, 50)
    ctx.fill();
    ctx.stroke();
    console.log("mouseclick registered at ", mouseX, mouseY);
}

//var drawCircle = function(e) {
var drawCircle = (e) => {
    var mouseX = e.offsetX;
    var mouseY = e.offsetY;
    ctx.beginPath()
    ctx.arc(mouseX, mouseY, 50, 0, 2 * Math.PI);
    ctx.fill();
    ctx.stroke();
    console.log("mouseclick registered at ", mouseX, mouseY);
}

//var draw = function(e) {
var draw = (e) => {
  if (mode == "rect") {
    drawRect(e);
  }
  else {
    drawCircle(e);
  }
}

//var wipeCanvas = function() {
var wipeCanvas = () => {
    console.log("wiping?");
    ctx.clearRect(0,0, c.width, c.height);
}

c.addEventListener("click", draw)
var bToggler = document.getElementById("buttonToggle")
bToggler.addEventListener("click", toggleMode);
var clearB = document.getElementById("buttonClear");
clearB.addEventListener("click", wipeCanvas);
