// Helper function - gets last letter of string and
// returns a new string using that letter (used to
// transform label ids into form ids and back)
function transformId(id, newPrefix) {

    var letter = id.slice(-1);
    return (newPrefix + letter);

}

// When document is loaded
$(document).ready(function() {

    // For the notes page only
    if ($("#critique").length) {

        // Position the labels on document load, set class and fade in
        $("ul#edit-list li").each(function() {
            // Get the form and the letter from the form id
            var form = $(this).children("form");
            var form_id = form.attr('id');

            // Skip the new note form
            if (form_id != "form-new") {
                // Grab the label we'll update
                var label_id = transformId(form_id, "label-")
                var label = $("#" + label_id);

                // Get the initial position and image height from the form
                var init_pos_x = form.children("input[name=pos_x]").val();
                var init_pos_y = form.children("input[name=pos_y]").val();
                var img_h = form.children("input[name=height]").val();

                // If the initial position is the top left corner, we
                // won't do anything except fade it in
                if (init_pos_x * init_pos_y != 0) {

                    // Compute the scale factor - we know the height is
                    // 400px
                    var scale = 400 / img_h;

                    // Scale the coordinates and position the label
                    var scaled_pos_x = parseInt(init_pos_x * scale);
                    var scaled_pos_y = parseInt(init_pos_y * scale);
                    label.css({top: scaled_pos_y, left: scaled_pos_x});

                    // Set the class to "done" if needed
                    if ($(this).children("form").children("span").hasClass("done")) {
                        label.addClass("done");
                        $(this).children("form").children("label").addClass("done");
                    }

                }

                // Fade in quickly
                label.fadeTo(100, 1);
        
            }
            
        });

        // Make image labels draggable
        $("#image-labels li").draggable({
            containment: '#image img',
            stack: "#image-labels li",
            stop: function(event, ui) {
                // Get the ending position of the label
                var pos_x = parseInt( ui.position.left );
                var pos_y = parseInt( ui.position.top );

                // Grab the form we'll update
                var form_id = transformId($(this).attr('id'), "form-")
                var form = $("#" + form_id);

                // Get the height of the image (before CSS) - if we
                // get it from the form, we don't have to wait for
                // the image to load
                var img_h = form.children("input[name=height]").val();

                // Compute the scale factor - we know the height is
                // 400px
                var scale = img_h / 400;

                // Scale the position to fit the actual size
                // of the image
                var scaled_pos_x = parseInt(pos_x * scale);
                var scaled_pos_y = parseInt(pos_y * scale);

                // Update the position input fields
                form.children("input[name=pos_x]").val(scaled_pos_x);
                form.children("input[name=pos_y]").val(scaled_pos_y);

                // Submit the form
                form.submit();
            }
        });

    }

    // Make title/text editable when double-clicked, unless completed
    $("ul#edit-list li form span").dblclick(function(e) {

        if (!$(this).hasClass("done")) {

            $(this).hide();
            $(this).siblings(":checkbox.complete + label").hide();
            $(this).siblings(":checkbox.delete + label").show();
            $(this).siblings(":text").show();
            $(this).siblings("textarea").show();

        }

    }); 

    // Handles new note/edited note submit
    $("textarea").keypress(function(e) {

        if (e.which == 13) {

            $(this).parent().submit();

        }

    });

    // Handles note complete
    $("#note-area :checkbox.complete + label").click(function(e) {

        var checkbox = $(this).siblings("input[name=isCompleted]");

        if (checkbox.is(":checked")) {
            checkbox.prop('checked', false);
        }
        else {
            checkbox.prop('checked', true);
        }

        $(this).parent().submit();

    });

    // Handles note delete
    $("#note-area li form :checkbox.delete + label").click(function(e) {

        $(this).siblings("input[name=delete]").prop('checked', true);
        $(this).parent().submit();

    }); 

    // Handles critique item delete
    $("#home-area li form :checkbox + label").click(function(e) {

        $(this).siblings("input[name=delete]").prop('checked', true);
        $(this).parent().submit();

    }); 

    // Click anywhere else on page to exit edit mode
    $(document).click(function(e) { 

        if (!$(e.target).closest("ul#edit-list li form :text").length &&
            !$(e.target).closest("ul#edit-list li form textarea").length &&
            !$(e.target).closest("ul#edit-list li form :checkbox + label").length) {

            $("ul#edit-list li form span").show();
            $("ul#edit-list li form .hidden").hide();
            $("ul#edit-list li form :checkbox.complete + label").show();

        }   

    });

    // Set focus on empty input field
    if ($("#id_text").length) {
        $("#id_text").focus();
    }

});