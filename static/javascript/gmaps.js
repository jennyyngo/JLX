var map;
var marker;
var infowindows = [];


function initMap() {
  map = new google.maps.Map(document.getElementById('map'), {
    center: {lat: 49.27899252, lng: -123.13000000},
    zoom: 14
  });
}




function plotFoodTruck(latitude, longitude, businessName, slug) {
	var marker = new google.maps.Marker({
    position: {lat: latitude, lng: longitude}, 
    map: map,
    title: businessName,
	slug: slug,

  });

var contentString = '<div id="content">'+
      '<div id="siteNotice">'+
      '</div>'+
      '<h3 id="firstHeading" class="firstHeading">'+businessName+'<br>'+
'<a href="/GrubHunt/find_route/' + marker.slug + '">'+"(Food Truck Vendor)"+'</a>'+'</h3>'+
      '</div>';

  var infowindow = new google.maps.InfoWindow({
    content: contentString
  });

// gather all info windows so you can close them before opening a new one.
infowindows.push(infowindow);


  google.maps.event.addListener(marker, 'click', function() {
//     _.each(googlemap.infowindows, function(infowindow) {
//     infowindow.close();
// });
    closeInfowWindows();
    infowindow.setContent(contentString);
    infowindow.open(map, marker);

  });
}

function closeInfowWindows() {
  for (var i = 0; i < infowindows.length; i++) {
    infowindows[i].close();

  }
}




	


