$(document).ready(function () {

    function readURL(input) {
        if (input.files && input.files[0]) {
            var file = input.files[0];
            var fileType = file.type;
            var validImageTypes = ["image/jpeg", "image/png"];

            if ($.inArray(fileType, validImageTypes) < 0) {
                alert("Please select a valid image file (jpg, png).");
                $('#id_image').val("");
                return;
            }

            var reader = new FileReader();
            console.log("reader", reader);

            reader.onload = function (e) {
                $('#image-preview').attr('src', e.target.result);
                $('#image-preview-1').attr('src', e.target.result).css('display', 'block');
                $('#delete-image').css('display', 'block');
            };

            reader.readAsDataURL(file);
        }
    }

    $('#id_image').change(function () {
        if ($(this).val()) {
            readURL(this);
        } else {
            deleteImage();
        }
    });

    $('#delete-image').click(function () {
        deleteImage();
    });

    function deleteImage() {
        $('#image-preview').attr('src', image);
        $('#delete-image').css('display', 'none');
        $("#id_image").val("");

        if (!image) {
            $('#image-preview-1').attr('src', image).css('display', 'none');
        }
    }
});
