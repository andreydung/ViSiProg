var controller = (function () {

  var N_BATCH = 36;
  var N_GROUP = 9;
  var folderPath="/static/images/";
  var listPath="/static/list.txt";
  var listimage;
  var N_TOTAL;
  var prob = [];
  var inPool = [];
  var haveSeen = [];
  var Nshown = 0;

  var currentGroup = [];
  var previousGroup = [];

  var pressAllowed = true;
  var firstShuffle = true;

  function initializeArray(value, len) {
    // initialize an array of len with value
    var arr = [];
    for (var i = 0; i < len; i++) {
      arr.push(value);
    }
    return arr;  
  }

  function getRandomfromRange(min, max) {
    return Math.random() * (max - min) + min;
  }

  function randomFromPool() {
    // Pick a random image from the pool inPool, with probability prob.
    var sum = 0;
    for (var i = 0; i < N_TOTAL; i++) {
      sum = sum + inPool[i] * prob[i];
    }

    var random = getRandomfromRange(0, sum);
    var cum = 0;
    for (var i = 0; i < N_TOTAL; i++) {
      cum += inPool[i] * prob[i];
      if (cum > random)
        return i;
    }
    return N_TOTAL - 1;
  }

  function intersect(a, b) {
    // how many common elements between a and b
    a.sort();
    b.sort();

    var i = 0, j = 0;

    count = 0;
    while (i < a.length && j < b.length) {
      if (a[i] == b[j]) {
        count += 1;
        i += 1;
        j += 1;
      }
      else {
        if (a[i + 1] < b[j + 1])
          i += 1;
        else
          j += 1;
      }
    }
    return count;
  }

  function shuffleHelper(keptback) {
    // Don't shuffle image from group that are back to batch
    if (keptback == true)
      var imgBatch = $("#batch img").slice(0, N_BATCH - N_GROUP);
    else
      var imgBatch = $("#batch img");
    $.each(imgBatch, function() {
      var tmp = randomFromPool();
      $(this).attr({"src": folderPath.concat(listimage[tmp]),
                      "id": tmp})
    })
  }

  function Shuffle() {
    if ($('#group ul li').length < N_GROUP)
    {
      alert(" You must put 9 images in the group box!");
      return;
    }

    var currentGroup = $("#group img").map(function(){
      return $(this).attr("id");        
    }).get();

    // Store selection to local web storage
    console.log(currentGroup.toString());
    var tmp = localStorage.getItem("groups");
    localStorage.setItem("groups", tmp.concat(currentGroup.toString().concat(",end,")));

    // Change probability of shown images
    $("#batch img").map(function() {
      if (haveSeen[$(this).attr("id")] === 0) {
        haveSeen[$(this).attr("id")] = 1;
        Nshown += 1;
      }
      prob[$(this).attr("id")] /= 4;
    })
    
    $("#progress").text(Nshown.toString());

    if (firstShuffle) { 
      firstShuffle = false;
      previousGroup = currentGroup;     
      shuffleHelper(false);
    }
    else
    {
      // Check how much overlap with previous group
      if (intersect(previousGroup, currentGroup) < N_GROUP/2) {
        
        // remove this images from Pool
        $("#group img").map(function() {
          if (inPool[$(this).attr("id")] === 1) {
            inPool[$(this).attr("id")] = 0;
          }
        });
        // Move all in Group back to Batch
        var imgGroup = $("#group ul li");
        $.each(imgGroup, function() {
          $("#batch").append($(this));
        })

        // Clear the Group box
        $("#group ul li").remove();

        // shuffle image from batch only
        shuffleHelper(true);
      }
      else {
        shuffleHelper(false);
      }
    }
  }

  return {
    init: function(callback) {
      localStorage.clear();
      localStorage.setItem("groups","");

      // Ajax request to read textfile
      $.get(listPath, function(data){
        listimage = data.split("\n");
        N_TOTAL = listimage.length;
        Nshown = 0;

        prob = initializeArray(1, N_TOTAL);
        inPool = initializeArray(1, N_TOTAL);
        haveSeen = initializeArray(0, N_TOTAL);

        for (i = 0; i < N_BATCH; i++) {
          var tmp = randomFromPool();
         // $("#batch").append('<li class="ui-widget-content ui-corner-tr"> <img src="images/001.png" width="128" height="128"> </li>');
          $("#batch").append(
            $("<li>").attr({'class': 'ui-widget-content ui-corner-tr'}).append(
              $("<img>").attr({src: folderPath.concat(listimage[tmp]), 'id': tmp})));
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
        }
        else {
          $group.droppable("enable");
      }
      });

      $("#ShuffleButton").on("click", Shuffle);
      $(window).keypress(function(e) {
        e.preventDefault();
        if (!pressAllowed) 
          return;
        pressAllowed = false;
        if (e.keyCode == 0 || e.keyCode == 32) {
          Shuffle();  
        }
      });

      $(window).keyup(function(e) {
        pressAllowed = true;
      });
      
      function Submit() {
        // send result to server
      }
    }
  };
}) ();
