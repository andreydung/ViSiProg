var controller = (function () {

  var taskpage;

	var N_BATCH = 36;
	var N_GROUP = 9;
	var folderPath="/static/images/";
	var listPath="/static/list.txt";
	var listimage;
	var N_TOTAL;

  var listshuffle = function(a) {
    for (var j, x, i = a.length; i; j = Math.floor(Math.random() * i), x = a[--i], a[i] = a[j], a[j] = x);
    return a;
  };

	return {
		init: function(callback) {
			localStorage.clear();
			localStorage.setItem("groups","");

			// Ajax request to read textfile
			$.get(listPath, function(data){
				listimage = data.split("\n");
				N_TOTAL = listimage.length;
				listimage = listshuffle(listimage);

				for (i = 0; i < N_BATCH; i++) {
				 // $("#batch").append('<li class="ui-widget-content ui-corner-tr"> <img src="images/001.png" width="128" height="128"> </li>');
					$("#batch").append(
						$("<li>").attr({'class': 'ui-widget-content ui-corner-tr'}).append(
							$("<img>").attr({src: folderPath.concat(listimage[i])})));
				};
        callback();
			})
    },

    makeUIactions: function() {
      var $batch = $("#batch"), $group = $("#group");
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

      $(document).on("mousedown", function () {
        if ($('#group ul li').length >= N_GROUP) {
          $group.droppable("disable");
          console.log("Disabled")
        }
        else {
          $group.droppable("enable");
          console.log("Enabled")
      }
      });

      document.getElementById("ShuffleButton").addEventListener("click", ShuffleBatch);
			// $("#ShuffleButton").on("click", ShuffleBatch);

			function ShuffleBatch() {
				// reset group and store result
				if ($('#group ul li').length < N_GROUP)
				{
					alert(" You must put 9 images in the group box!");
				}
				else
				{
					var imagegroup = $("#group img").map(function(){
						return $(this).attr("src").split("/").pop();				
					}).get();
					console.log(imagegroup.toString());
					console.log(imagegroup);

					var tmp = localStorage.getItem("groups").toString();
					localStorage.setItem("groups", tmp.concat(imagegroup.toString().concat(", end, ")));
				}
			}

			function Submit() {
				// send result to server
			}
		}
	};
}) ();
