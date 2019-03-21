$(document).ready( function() {
	$("#vehicle_form").hide();
	$("#z_pic").hide();
	$("#m_pic").hide();
	$("#s_pic").hide();
	$("#d_pic").hide();
	$("#slide").hide();
	$("#account_email").hide();
	$("#account_name").hide();
	$("#reviews").hide();
	
	$("#open_sell").click( function(event) {
		$("#vehicle_form").slideToggle(500);
	});
	$("#zander").hover( function(event) {
		$("#z_pic").fadeIn(2000);
	});
	$("#deni").hover( function(event) {
		$("#d_pic").fadeIn(2000);
	});
	$("#sho").hover( function(event) {
		$("#s_pic").fadeIn(2000);
	});
	$("#micc").hover( function(event) {
		$("#m_pic").fadeIn(2000);
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

