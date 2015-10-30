
function find_route(from_pos, to_pos) {
        // Center initialized to vancouver
        var myOptions = {
          zoom: 14,
          center: new google.maps.LatLng(49.28449252, -123.1429261),
          mapTypeId: google.maps.MapTypeId.ROADMAP
        };
        // Draw the map
        var mapObject = new google.maps.Map(document.getElementById("map"), myOptions);

        var directionsService = new google.maps.DirectionsService();
        var directionsRequest = {
          origin: from_pos,
          destination: to_pos,
          travelMode: google.maps.DirectionsTravelMode.DRIVING,
          unitSystem: google.maps.UnitSystem.METRIC
        };
        directionsService.route(
          directionsRequest,
          function(response, status)
          {
            if (status == google.maps.DirectionsStatus.OK)
            {
              new google.maps.DirectionsRenderer({
                map: mapObject,
                directions: response
              });
            }
            else
              $("#error").append("Unable to retrieve your route<br />");
          }
        );
      }

function getlatlng(latitude,longitude){
	var lat = latitude;
	var lng = longitude;
}

$(document).ready(function() {
        // If the browser supports the Geolocation API
    if (typeof navigator.geolocation == "undefined") {
          $("#error").text("Your browser doesn't support the Geolocation API");
          return;
    }

    $("#find_route").submit(function(event) {
	    event.preventDefault();
		// auto fill the origin with user's current location if origin is not filled
	    if($("#from_pos").val() == ""){
		    navigator.geolocation.getCurrentPosition(function(position){
		    var geocoder = new google.maps.Geocoder();
		    geocoder.geocode({
			    "location": new google.maps.LatLng(position.coords.latitude, position.coords.longitude)
		    },
		function(results, status){
			if(status == google.maps.GeocoderStatus.OK)
				$("#from_pos").val(results[0].formatted_address);
			else$("#error").append("Unable to retrive your location<br/>");
		});
	});
		// NOT CORRECT YET
		// auto fill the destination with vendor's latlng if destination is not filled
	    }if($("#to_pos").val() == ""){
		    //TODO: get the auto_position passed in
		    //find_route($("#from_pos").val(),marker.position());			
		    $("#to_pos").val(new google.maps.LatLng(getlatlng.lat, getlatlng.lng));
			$("#error").append("to_pos is null<br />");
	    }else{
	        find_route($("#from_pos").val(), $("#to_pos").val());
	    }
	});
});