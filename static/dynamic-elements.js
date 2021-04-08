$(document).ready(function() {

	// These functions deal with the profile bar at the top of every page; be it
	// through hiding and showing the different types of bar, or through sending
	// the actual request that changes the profile ID for a given session.

	$("a[function=show-profilebar-dynamic]").click(function(event){
		$("#profilebar-static").attr("style","display:none");
		$("#profilebar-dynamic").attr("style","");
		event.preventDefault();
	});

	$("a[function=show-profilebar-static]").click(function(event){
		$("#profilebar-dynamic").attr("style","display:none");
		$("#profilebar-static").attr("style","");
		event.preventDefault();
	});

	$("[function=change-profile-id]").click(function(event){
		$("#profilebar-error").attr("style","display:none");
		$.ajax({url:"/change-profile-id", method:"POST", data:{"profile_id":$("input#profile-id-input").val()}}).done(function(data){
			response = JSON.parse(data);
			if(response.success){
				location.reload();
			} else {
				$("#profilebar-error").attr("style","");
			}
		});
		event.preventDefault();
	});



	// These functions deal with dynamically showing and hiding the main menu
	// subcategory dropdowns.

	$(".menuitem").hover(function(){
		$(".menudropdown").attr("style","display:none");
		$("#"+$(this).attr("dropdown")).attr("style","display:block");
	}, function(){});

	$("#menuwrapper").hover(function(event){}, function(){
		$(".menudropdown").attr("style","display:none");
	})

	// This function submits the request for adding items to the shopping cart.

	$("a[function=add-to-shopping-cart]").click(function(event){
		$.ajax({url:"/add-to-shopping-cart", method:"POST", data: {"product_id": $(this).attr("productid")}}).done(function(data){
			response = JSON.parse(data);
			if(response.success){
				$("#shoppingcartcount").html(response.itemcount);
			}
		});
		event.preventDefault();
	});

	$("a[function=remove-from-shopping-cart]").click(function(event){
		$.ajax({url:"/remove-from-shopping-cart", method:"POST", data: {"product_id": $(this).attr("productid")}}).done(function(data){
			response = JSON.parse(data);
			if(response.success){
				$("#shoppingcartcount").html(response.itemcount);
			}
		});
		event.preventDefault();
	});

	$("a[function=get-products-from-keuzevraag]").click(function(event){
		// zo pak je de input van de user choise
		var optie_1 = $('#optie').find(":selected").text();
		var optie_2 = $('#optie_2').find(":selected").text();
		var optie_3 = $('#optie_3').find(":selected").text();

		$.ajax({url:"/get-products-from-keuzevraag", method:"POST", data: {"optie_1": optie_1, "optie_2": optie_2, "optie_3": optie_3}}).done(function(data){
			response = JSON.parse(data);
			if(response.success){
				window.location = response.refurl;
			}
		});
		event.preventDefault();
	});


	// This function submits the request for changing the displayed number of
	// items per page.

	$("select#pagination-select").change(function(){
		$.ajax({url:"/producten/pagination-change", method:"POST", data:{"refurl": window.location.pathname, "items_per_page": $(this).val()}}).done(function(data){
			response = JSON.parse(data);
			if(response.success){
				window.location.href = response.refurl;
			}
		});
	});

	document.getElementById("open-popup-btn").addEventListener("click",function(){
	document.getElementsByClassName("popup")[0].classList.add("active");
	});

	document.getElementById("dismiss-popup-btn").addEventListener("click",function(){
		document.getElementsByClassName("popup")[0].classList.remove("active");
	});


});
