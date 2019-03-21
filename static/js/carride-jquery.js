$(document).ready( function() {
	$("#vehicle_form").hide();
	
	$("#slide").hide();
	$("#account_email").hide();
	$("#account_name").hide();
	$("#reviews").hide();
	
	$("#open_sell").click( function(event) {
		$("#vehicle_form").slideToggle(500);
	});
	
	
	$("#picture").click( function(event) {
		$("#account_name").slideToggle(500);
		$("#account_email").slideToggle(500);
		
		$("#account_cars").slideToggle(500);
	});
	$("#slide_title").click( function(event) {
		$("#slide").slideToggle(500);
	});
	$("#open_reviews").click( function(event) {
		$("#reviews").slideToggle(500);
	});

});

