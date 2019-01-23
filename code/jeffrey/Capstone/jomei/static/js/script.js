var blueIcon = new L.Icon({
	iconUrl: 'static/img/marker-icon-2x-blue.png',
	shadowUrl: 'static/img/marker-shadow.png',
	iconSize: [25, 41],
	iconAnchor: [12, 41],
	popupAnchor: [1, -34],
	shadowSize: [41, 41]
});

var redIcon = new L.Icon({
	iconUrl: 'static/img/marker-icon-2x-red.png',
	shadowUrl: 'static/img/marker-shadow.png',
	iconSize: [25, 41],
	iconAnchor: [12, 41],
	popupAnchor: [1, -34],
	shadowSize: [41, 41]
});

var greenIcon = new L.Icon({
	iconUrl: 'static/img/marker-icon-2x-green.png',
	shadowUrl: 'static/img/marker-shadow.png',
	iconSize: [25, 41],
	iconAnchor: [12, 41],
	popupAnchor: [1, -34],
	shadowSize: [41, 41]
});

var orangeIcon = new L.Icon({
	iconUrl: 'static/img/marker-icon-2x-orange.png',
	shadowUrl: 'static/img/marker-shadow.png',
	iconSize: [25, 41],
	iconAnchor: [12, 41],
	popupAnchor: [1, -34],
	shadowSize: [41, 41]
});

var yellowIcon = new L.Icon({
	iconUrl: 'static/img/marker-icon-2x-yellow.png',
	shadowUrl: 'static/img/marker-shadow.png',
	iconSize: [25, 41],
	iconAnchor: [12, 41],
	popupAnchor: [1, -34],
	shadowSize: [41, 41]
});

var violetIcon = new L.Icon({
	iconUrl: 'static/img/marker-icon-2x-violet.png',
	shadowUrl: 'static/img/marker-shadow.png',
	iconSize: [25, 41],
	iconAnchor: [12, 41],
	popupAnchor: [1, -34],
	shadowSize: [41, 41]
});

var greyIcon = new L.Icon({
	iconUrl: 'static/img/marker-icon-2x-grey.png',
	shadowUrl: 'static/img/marker-shadow.png',
	iconSize: [25, 41],
	iconAnchor: [12, 41],
	popupAnchor: [1, -34],
	shadowSize: [41, 41]
});

var blackIcon = new L.Icon({
	iconUrl: 'static/img/marker-icon-2x-black.png',
	shadowUrl: 'static/img/marker-shadow.png',
	iconSize: [25, 41],
	iconAnchor: [12, 41],
	popupAnchor: [1, -34],
	shadowSize: [41, 41]
});

let iconList = [blueIcon,blackIcon,greyIcon,violetIcon,yellowIcon,orangeIcon,greenIcon,redIcon];

let iconChoiceOthers = iconList[Math.floor(Math.random() * iconList.length)];
let iconChoiceUser = iconList[Math.floor(Math.random() * iconList.length)];

let truth = true;

let
  map,
  newMarker,
  savedMarkers,
  newPoint1,
  savedPoint,
  popString,
  myLocation,
  distanceAway,
  myCoordinates,
  markerCoordinates,
  popName,
  distanceString,
  distance_string,
  private_btn,
  sync_btn,
  universal_btn,
  otherSavedMarkers,
  unsavedMarkers;

unsavedMarkers = [];
savedMarkers = [];
otherSavedMarkers = [];

let test = false;

let saved_user_markers_data = JSON.parse(document.getElementById('user_marker_data').textContent);
let saved_other_user_markers_data = JSON.parse(document.getElementById('others_marker_data').textContent);

console.log(saved_user_markers_data);
console.log(saved_other_user_markers_data);

// this function will add all of the pre-existing markers to the map
function addToMap(locationArray){

  //iterates through the array object called from the server
  [].forEach.call(locationArray, function(location){

      savedMarkers[location.id] = L.marker([location.latitude, location.longitude], {icon: iconChoiceUser}).addTo(map)}
      )
    };

// this function will add all of the pre-existing markers to the map
function addToMapOthers(locationArray){

  //iterates through the array object called from the server
  [].forEach.call(locationArray, function(location){

      otherSavedMarkers[location.id] = L.marker([location.latitude, location.longitude],{icon: iconChoiceOthers}).addTo(map)}
      )
      console.log(otherSavedMarkers);
    };

// button defs
private_btn = document.getElementById('private_btn');
sync_btn = document.getElementById('sync_btn');
universal_btn = document.getElementById('universal_btn');

universal_btn.addEventListener('click', function(){
  addToMapOthers(saved_other_user_markers_data);
  console.log(saved_other_user_markers_data);
})

private_btn.addEventListener('click', function(){
  map.remove();
  initialize();
});

function initialize(){
  map = L.map('map').setView([45.527453, -122.668923], 10)

  L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token=pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpejY4NXVycTA2emYycXBndHRqcmZ3N3gifQ.rJcFIG214AriISLbB6B5aw', {
      maxZoom: 18,
      attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, ' +
          '<a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, ' +
          'Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
      id: 'mapbox.outdoors'
  }).addTo(map);

  addToMap(saved_user_markers_data);

  // allows the user to find their own location using the easybutton
  L.control.locate({
    flyTo: true,
    showPopup: false,
    locateOptions: {enableHighAccuracy: true, maxZoom: 15},
    strings: {title: "Find current location"},
    follow: false
  }).addTo(map);

  // when location is found adds to map
  function onLocationFound(e) {
    myLocation = L.marker(e.latlng).remove();
    var radius = e.accuracy / 2;

    myLocation = L.marker(e.latlng).addTo(map).bindPopup("You are within " + radius + " meters from this point").openPopup();
    L.circle(e.latlng, radius).addTo(map);
    myCoordinates = e.latlng;
    myCoordinates = Object.values(myCoordinates);
  }

  // alert if cannot find location
  function onLocationError(e) {
    alert(e.message);
  }

  function addMarker(e){
  // Add marker to map at click location; add popup window

    newMarker = new L.marker(e.latlng).addTo(map);

    // input the form into the popup
    // input text field
    let name_field = document.createElement("input");
    name_field.id = "name_field";
    name_field.type = "text";
    name_field.placeholder = "Marker name";

    // input text area for tags
    let tags_field = document.createElement("textarea");
    tags_field.id = 'tag_field';
    tags_field.placeholder = "Place # separated tags here";

    // boolean public or not
    let public_layer_checkbox = document.createElement('input');
    public_layer_checkbox.type = "checkbox";
    public_layer_checkbox.id = "public_check";
    let checkbox_label = document.createElement('label');
    checkbox_label.htmlFor = "public_check";
    checkbox_label.appendChild(document.createTextNode('Private'));

    // create submit button
    let pop_submit_btn = document.createElement("input");
    pop_submit_btn.type = "submit";
    pop_submit_btn.addEventListener('click', function(){
      listNewMarker();
      // postMarker();
    });

    // add form elements to a flexbox
    let pop_form = document.createElement("li");
    pop_form.style.display = "flex";
    pop_form.style.flexDirection = "column";
    pop_form.appendChild(name_field);
    pop_form.appendChild(tags_field);
    pop_form.appendChild(public_layer_checkbox);
    pop_form.appendChild(checkbox_label);
    pop_form.appendChild(pop_submit_btn);
    console.log(pop_form);

    newMarker.bindPopup(pop_form).openPopup();
    document.getElementById('name_field').focus();
    document.getElementById('name_field').select();

    // adds the new marker onto the map
    // markers.push(newMarker);
    console.log(newMarker);
  }

  let toModel_Marker_Data;

  function listNewMarker(){
    // creates the flexbox and gets content for putting markers onto the list
    // should this only be added to the list once a marker is saved
    popString = document.createElement("li");
    popString.style.display = "flex";
    // popString.innerHTML += newMarker._popup.getContent();
    console.log(newMarker['_latlng']);

    // change the name but make these the DELETE buttons
    let select_mark_checkbox = document.createElement("input");
    select_mark_checkbox.type = "checkbox";

    // adds the checkbox and the latlng information to the markers list
    popString.appendChild(select_mark_checkbox);
    newPoint1.appendChild(popString);

    // adds the newMarker's latlng object to the markerCoordinates variable for calculating distance from origin
    markerCoordinates = newMarker['_latlng'];
    markerCoordinates = Object.values(markerCoordinates);
    console.log("markerCoordinates for caluclating distance are: ",markerCoordinates);

    // prepares the data for sending to the database
    toModel_Marker_Data = newMarker.getLatLng();
    toModel_Marker_Data['name'] = document.getElementById('name_field').value;
    toModel_Marker_Data['tag'] = document.getElementById('tag_field').value;
    toModel_Marker_Data['layer'] = document.getElementById('public_check').value;

    // set distance = 0 is origin is not defined
    let distance = 0;
    let distancePrint = 0;

    if (myCoordinates === undefined){
      // if myCoordinates not set then can't find distance
      distance_string = "your location was undefined";
      distanceString = document.createElement("li");
      distanceString.style.display = "flex";
      distancePrint = distance_string;
      distanceString.innerHTML += distance_string;
    } else {
      // find the distance
      distance = getDistance(myCoordinates, markerCoordinates);
      distanceString = document.createElement("li");
      distanceString.style.display = "flex";
      distanceString.innerHTML += distance + " meters";
      distancePrint = `${distance} meters`;
    }

    // Adding of newly created points to "Recently Added to Map" section
    popString.innerHTML +=
      String(document.getElementById('name_field').value) +
      " Lat: " + String((newMarker['_latlng']['lat']).toFixed(5)) +
      " Long: " + String((newMarker['_latlng']['lng']).toFixed(5)) +
      " Distance away: " + String(distancePrint);

    console.log("distance = ", distance);
    // // adds distance to the Marker_data object
    toModel_Marker_Data['distance_away'] = distance;
    console.log("toModel_Marker_Data ",toModel_Marker_Data);
    unsavedMarkers.push(toModel_Marker_Data);
    console.log(unsavedMarkers);
  }

  // // posts the new marker data to the
  // function postMarker(){
  //   axios.post('newmarker/', toModel_Marker_Data)
  // .then(function (response) {
  //   console.log(response);
  // })
  // .catch(function (error) {
  //   alert("Was not able to save this marker.")
  //   console.log(error);
  // });
  // }

  map.on('locationfound', onLocationFound);
  map.on('locationerror', onLocationError);
  map.on('click', addMarker);

  newPoint1 = document.createElement("div");
  newPoint1.style.display = "flex";
  newPoint1.style.justifyContent = "space-evenly";
  newPoint1.style.flexDirection = "column";
  newPoint1.style.width = "100%";
  newPoint1.style.marginTop = "5px";

  target2 = document.getElementById("Created_Target");
  target2.appendChild(newPoint1);
}

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

// deletes the savedPoint
function deleteSavedPoint(line,div){
  axios.post(`deletemarker/${line}/`)
  // best practice would be to add the delete function here after the '.then' so that it all in one swoop deletes the div if successful
    .then(function(response){
    console.log(response);
    div.remove();
    savedMarkers[line].remove();
    })
    .catch(function(error){
      alert("Was not able to delete this point.")
      console.log(error);
    });
  };

// updates saved points list
function updatSPL(){
  if (saved_user_markers_data){
    for (let i=0; i<saved_user_markers_data.length; i++){

      let pList = saved_user_markers_data;
      console.log(pList);
      let pointIndex = i+1;
      let pointID = pList[i].id;
      console.log("PointID =",pointID)
      console.log(pointIndex);
      let pointName = pList[i].name;
      console.log(pointName);
      let pointTags = pList[i].tag;
      console.log(pointTags);
      let pointSet = `#${pointIndex} Name: ${pointName} Tags: ${pointTags}`;


      savedPoint = document.createElement("div");
      // savedPoint.id =
      savedPoint.style.display = "flex";
      savedPoint.style.justifyContent = "space-evenly";
      savedPoint.style.flexDirection = "row";
      savedPoint.style.width = "100%";
      savedPoint.style.marginTop = "5px";
      savedPoint.innerHTML += pointSet;

      let saved_point_delete_btn = document.createElement('input');
      saved_point_delete_btn.type = "button";
      saved_point_delete_btn.value = "Delete";
      saved_point_delete_btn.addEventListener('click', function(){
        deleteSavedPoint(pointID, this.parentElement);
      });

      target1 = document.getElementById("Saved_Target");
      target1.appendChild(savedPoint);
      // this puts the div inside the div for easier targeted deleting
      savedPoint.appendChild(saved_point_delete_btn);

    }
  }
}

updatSPL();

initialize();

// posts the new marker data to the
  function postMarker(point){
    axios.post('newmarker/', point)
  .then(function (response) {
    console.log(response);
  })
  .catch(function (error) {
    alert("Was not able to save this marker.")
    console.log(error);
  });
  }
let interval;

function reload(){
  document.getElementById('reload').click();
}

sync_btn.addEventListener('click', function(){
  if (unsavedMarkers.length >0){
    for (i=0; i<unsavedMarkers.length;i++){
      postMarker(unsavedMarkers[i]);
      interval = setTimeout(reload,5);
    }
  } else {
    interval = setTimeout(reload,5);
  }
})



// let searchBar = document.getElementById('search-bar');
// searchBar.addEventListener('change', searchTags);

// let x;

// function searchTags(x){
//   x = searchBar.value;
//   console.log(x);
//   map.remove();
//   for (i=0; i<savedMarkers.length; i++){
//     if (savedMarkers[i]['tag'].includes(x)){
//       addToMap(savedMarkers[i]);
//     }
//   }
//   if (x.length<1){
//     initialize();
//   }
// }