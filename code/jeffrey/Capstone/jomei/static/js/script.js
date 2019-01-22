let truth = true;

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

let saved_user_markers_data = JSON.parse(document.getElementById('marker_data').textContent);

console.log(saved_user_markers_data);

function initialize(){
  map = L.map('map').setView([45.527453, -122.668923], 10)

  L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token=pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpejY4NXVycTA2emYycXBndHRqcmZ3N3gifQ.rJcFIG214AriISLbB6B5aw', {
      maxZoom: 18,
      attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, ' +
          '<a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, ' +
          'Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
      id: 'mapbox.outdoors'
  }).addTo(map);

    // this function will add all of the pre-existing markers to the map
  function addToMap(locationArray){

    //iterates through the array object called from the server
    [].forEach.call(locationArray, function(location){

        marker = L.marker([location.latitude, location.longitude]).addTo(map)}
        )
      };

  addToMap(saved_user_markers_data);

  // find osmewhere to store the points list for referencing the IDs for deleting them


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
    name_field.type = "text";
    name_field.placeholder = "Marker name";

    // input text area for tags
    let tags_field = document.createElement("textarea");
    tags_field.placeholder = "Place # separated tags here";

    // boolean public or not
    let public_layer_checkbox = document.createElement('input');
    public_layer_checkbox.type = "checkbox";
    public_layer_checkbox.id = "public_check";
    let checkbox_label = document.createElement('label');
    checkbox_label.htmlFor = "public_check";
    checkbox_label.appendChild(document.createTextNode('Dubstep or nah'));

    // create submit button
    let pop_submit_btn = document.createElement("input");
    pop_submit_btn.type = "submit";
    pop_submit_btn.addEventListener('click', postMarker);

    // create delete button
    let pop_delete_btn = document.createElement('input');
    pop_delete_btn.type = "button";
    pop_delete_btn.value = "Delete";
    pop_delete_btn.addEventListener('click', deleteMarker);

    // add form elements to a flexbox
    let pop_form = document.createElement("li");
    pop_form.style.display = "flex";
    pop_form.style.flexDirection = "column";
    pop_form.appendChild(name_field);
    pop_form.appendChild(tags_field);
    pop_form.appendChild(public_layer_checkbox);
    pop_form.appendChild(checkbox_label);
    pop_form.appendChild(pop_submit_btn);
    pop_form.appendChild(pop_delete_btn);



    newMarker.bindPopup(pop_form).openPopup();

    // adds the new marker onto the map
    markers.push(newMarker);
    console.log(newMarker);
    // creates the flexbox and gets content for putting markers onto the list
    // should this only be added to the list once a marker is saved
    popString = document.createElement("li");
    popString.style.display = "flex";
    popString.innerHTML += newMarker._popup.getContent();

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
    let toModel_Marker_Data = newMarker.getLatLng();

    // set distance = 0 is origin is not defined
    let distance = 0;

    if (myCoordinates === undefined){
      // if myCoordinates not set then can't find distance
      distance_string = "your location was undefined";
      distanceString = document.createElement("li");
      distanceString.style.display = "flex";
      distanceString.innerHTML += distance_string;
      newPoint2.appendChild(distanceString);
    } else {
      // find the distance
      distance = getDistance(myCoordinates, markerCoordinates);
      distanceString = document.createElement("li");
      distanceString.style.display = "flex";
      distanceString.innerHTML += distance + " meters";
      newPoint2.appendChild(distanceString);
    }
    console.log("distance = ", distance);
    // // adds distance to the Marker_data object
    // let time = new Date().toLocaleString('en-GB', { hourCycle: 'h24' });
    toModel_Marker_Data['distance_away'] = distance;
    // toModel_Marker_Data['created_date'] = time;
    console.log(toModel_Marker_Data);

    // posts the new marker data to the
    function postMarker(){
      axios.post('newmarker/', toModel_Marker_Data)
    .then(function (response) {
      console.log(response);
    })
    .catch(function (error) {
      alert("Was not able to save this marker.")
      console.log(error);
    });
    }

    // deletes the marker
    function deleteMarker(){
      axios.post($`'deletemarker/' + <int:pk>`, marker)
        .then(function(response){
        console.log(response);
        })
        .catch(function(error){
          alert("Was not able to delete this marker.")
          console.log(error);
        });
      };
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

initialize();

