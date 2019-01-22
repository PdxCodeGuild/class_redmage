// var template = '<form id="popup-form">\
//   <label for="input-name">Name:</label>\
//   <input id="input-name" class="popup-input" type="text" />\
//   <label for="input-tag">Tags:</label>\
//   <input id="input-tag" class="popup-input" type="text" />\

//   <button id="button-submit" type="button">Save Changes</button>\
// </form>';

function layerClickHandler (e) {

  var marker = e.target,
      properties = e.target.feature.properties;

  if (marker.hasOwnProperty('_popup')) {
    marker.unbindPopup();
  }

  marker.bindPopup(template);
  marker.openPopup();

  L.DomUtil.get('value-arc').textContent = properties.arc;
  L.DomUtil.get('value-speed').textContent = properties.speed;

  var inputSpeed = L.DomUtil.get('input-speed');
  inputSpeed.value = properties.speed;
  L.DomEvent.addListener(inputSpeed, 'change', function (e) {
    properties.speed = e.target.value;
  });

  var buttonSubmit = L.DomUtil.get('button-submit');
  L.DomEvent.addListener(buttonSubmit, 'click', function (e) {
    marker.closePopup();
  });

}



var map = L.map('leaflet', {
  'center': [0, 0],
  'zoom': 0,
  'layers': [
    L.tileLayer('http://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}.png', {
      attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, &copy; <a href="http://cartodb.com/attributions">CartoDB</a>'
    }),
    L.geoJson({
      "type": "FeatureCollection",
      "features": [{
        "type": "Feature",
        "geometry": {
          "type": "Point",
          "coordinates": [0,0]
        },
        "properties": {
          "arc": 321,
          "speed": 123
        }
      }]
    }, {
      onEachFeature: function (feature, layer) {
        layer.on('click', layerClickHandler);
      }
    })
  ]
});