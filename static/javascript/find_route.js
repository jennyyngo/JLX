
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


$(document).ready(function() {
        // If the browser supports the Geolocation API
    if (typeof navigator.geolocation == "undefined") {
          $("#error").text("Your browser doesn't support the Geolocation API");
          return;
    }
	
	// retrive user's current location
	$("#cur_loc").click(function(event){
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
	});
	
	
    $("#find_route").submit(function(event) {
	    event.preventDefault();
	    find_route($("#from_pos").val(), $("#to_pos").val());
	});
});