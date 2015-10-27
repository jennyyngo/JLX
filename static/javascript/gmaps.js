var map;


function initMap() {
  map = new google.maps.Map(document.getElementById('map'), {
    center: {lat: 49.28449252, lng: -123.1429261},
    zoom: 14
  });
}

function plotFoodTruck(latitude, longitude, businessName) {
	 var marker = new google.maps.Marker({
    position: {lat: latitude, lng: longitude}, 
    map: map,
    title: businessName

  });

var contentString = '<div id="content">'+
      '<div id="siteNotice">'+
      '</div>'+
      '<h3 id="firstHeading" class="firstHeading">'+businessName+'</h3>'+
      '</div>';

  var infowindow = new google.maps.InfoWindow({
    content: contentString
  });

  marker.addListener('click', function() {
    infowindow.open(map, marker);
  });
}




	


