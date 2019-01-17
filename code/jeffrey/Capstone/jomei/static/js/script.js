

let
  map,
  newMarker,
  markers,
  newPoint1,
  newPoint2,
  popString,
  myLocation,
  distanceAway,
  myCoordinates,
  markerCoordinates,
  popName,
  distanceString,
  distance_string;

markers = [];

let test = false;

function initialize() {
  map = L.map('map').setView([45.527453, -122.668923], 10)

  L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token=pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpejY4NXVycTA2emYycXBndHRqcmZ3N3gifQ.rJcFIG214AriISLbB6B5aw', {
      maxZoom: 18,
      attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, ' +
          '<a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, ' +
          'Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
      id: 'mapbox.outdoors'
  }).addTo(map);

  L.control.locate({
    flyTo: true,
    showPopup: false,
    locateOptions: {enableHighAccuracy: true, maxZoom: 15},
    strings: {title: "Find current location"},
    follow: false
  }).addTo(map);

  function onLocationFound(e) {
    myLocation = L.marker(e.latlng).remove();
    var radius = e.accuracy / 2;

    myLocation = L.marker(e.latlng).addTo(map).bindPopup("You are within " + radius + " meters from this point").openPopup();
    console.log(myLocation);
    L.circle(e.latlng, radius).addTo(map);
    myCoordinates = e.latlng;
    console.log(myCoordinates);
    myCoordinates = Object.values(myCoordinates);
    console.log("myCoordinates is", myCoordinates);
  }
  console.log("myLocation is ",myLocation);


  function onLocationError(e) {
    alert(e.message);
  }

  function addMarker(e){
  // Add marker to map at click location; add popup window

    newMarker = new L.marker(e.latlng).addTo(map);
    newMarker.bindPopup(`${newMarker.getLatLng()}`).openPopup();
    markers.push(newMarker);
    popString = document.createElement("li");
    popString.style.display = "flex";
    popString.innerHTML += newMarker._popup.getContent();

    let compareBtn = document.createElement("input");
    compareBtn.type = "checkbox";

    popString.appendChild(compareBtn);
    newPoint1.appendChild(popString);

    markerCoordinates = newMarker['_latlng'];
    markerCoordinates = Object.values(markerCoordinates);
    console.log("markerCoordinates is", markerCoordinates);

    let toModel_Marker_Data = newMarker.getLatLng();

    let distance = 0;

    if (myCoordinates === undefined){
      distance_string = "your location was undefined";
      distanceString = document.createElement("li");
      distanceString.style.display = "flex";
      distanceString.innerHTML += distance_string;
      newPoint2.appendChild(distanceString);
    } else {
      distance = getDistance(myCoordinates, markerCoordinates);
      distanceString = document.createElement("li");
      distanceString.style.display = "flex";
      distanceString.innerHTML += distance + " meters";
      newPoint2.appendChild(distanceString);
    }

    console.log("distance = ", distance);

    toModel_Marker_Data['distance_away'] = distance;

    axios.post('newmarker/', toModel_Marker_Data)
    .then(function (response) {
      console.log(response);
    })
    .catch(function (error) {
      alert("Was not able to save this marker.")
      console.log(error);
    });
  }

  map.on('locationfound', onLocationFound);
  map.on('locationerror', onLocationError);
  map.on('click', addMarker);

  newPoint1 = document.createElement("div");
  newPoint1.style.display = "flex";
  newPoint1.style.justifyContent = "space-evenly";
  newPoint1.style.flexDirection = "column";
  newPoint1.style.width = "100%";
  newPoint1.style.marginTop = "5px";

  target1 = document.getElementById("pointTarget");
  target1.appendChild(newPoint1);

  newPoint2 = document.createElement("div");
  newPoint2.style.display = "flex";
  newPoint2.style.justifyContent = "space-evenly";
  newPoint2.style.flexDirection = "column";
  newPoint2.style.width = "100%";
  newPoint2.style.marginTop = "5px";

  target2 = document.getElementById("distanceTarget");
  target2.appendChild(newPoint2);

};

let lat1, lat2, lng1, lng2,origin,destination;

function getDistance(origin, destination) {
  console.log("origin is", origin);

  // return distance in meters
  lon1 = toRadian(origin[1]);
  lat1 = toRadian(origin[0]);
  lon2 = toRadian(destination[1]);
  lat2 = toRadian(destination[0]);

  let deltaLat = lat2 - lat1;
  let deltaLon = lon2 - lon1;

  let a = Math.pow(Math.sin(deltaLat/2), 2) + Math.cos(lat1) * Math.cos(lat2) * Math.pow(Math.sin(deltaLon/2), 2);
  let c = 2 * Math.asin(Math.sqrt(a));
  let EARTH_RADIUS = 6371;
  return Math.round(c * EARTH_RADIUS * 1000);

}

function toRadian(degree) {
  return degree*Math.PI/180;
}

initialize();

