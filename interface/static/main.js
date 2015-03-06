$(function() {

		var folderPath="/static/images/";
		var listPath="/static/list.txt";

		$.get(listPath, function(data){
			window.listimage = data.split("\n");
			window.N_TOTAL = window.listimage.length;
			window.listimage = listshuffle(window.listimage);
			// console.log(window.listimage);

			for (i = 0; i < N_BATCH; i++) {
			 // $("#batch").append('<li class="ui-widget-content ui-corner-tr"> <img src="images/001.png" width="128" height="128"> </li>');
				$("#batch").append(
					$("<li>").attr({'class': 'ui-widget-content ui-corner-tr'}).append(
						$("<img>").attr({src: folderPath.concat(listimage[i])})));
			};

			// draggable batch
			$( "li", $batch ).draggable({
				revert: "invalid", // when not dropped, the item will revert back to its initial position
				containment: "document",
				helper: "clone",
				cursor: "move"
			});

			// droppable group
			$group.droppable({
				accept: "#batch > li",
				activeClass: "ui-state-highlight",
				drop: function( event, ui ) {
					moveToGroup( ui.draggable );
				}
			});
			
			// droppable batch
			$batch.droppable({
				accept: "#group li",
				activeClass: "custom-state-active",
				drop: function( event, ui ) {
					moveToBatch( ui.draggable );
				}
			});
		})

		window.N_BATCH = 36;
		window.N_GROUP = 9;

		var $batch = $("#batch"),
			$group = $("#group");

		function listshuffle(a){
			for(var j, x, i = a.length; i; j = Math.floor(Math.random() * i), x = a[--i], a[i] = a[j], a[j] = x);
			return a;
		};


		$(document).bind("mousedown", function () {
			//console.log($('#group ul li').length);
			if ($('#group ul li').length >= window.N_GROUP)
				$group.droppable("disable");
			else
				$group.droppable("enable");
			});

		function Shuffle() {
			// reset group and store result
			$.post()

			// shuffle batch

		}

		function Submit() {
			// send result to server

		}

		function moveToGroup( $item ) {
			$item.fadeOut(function() {
				var $list = $( "ul", $group)
				$item.appendTo( $list ).fadeIn(function() {
					$item.find( "img" )
				});
			});
		}

		function moveToBatch( $item ) {
			$item.fadeOut(function() {
				$item.appendTo($batch).fadeIn();
			});
		}
	});