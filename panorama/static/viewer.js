
// create PanoViewer with option
var PanoViewer = eg.view360.PanoViewer;
var container = document.querySelector(".container");

var panoViewer = new PanoViewer(container, {
  projectionType: "cubemap",
  image: "static/panoramafull.png" });


PanoControls.init(document.querySelector(".viewer"), panoViewer);
PanoControls.showLoading();

