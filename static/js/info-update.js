$(document).ready(function () {


    function readURL(input) {
        if (input.files && input.files[0]) {
            var reader = new FileReader();

            reader.onload = function (e) {
                $('#image-preview').attr('src', e.target.result);
                $('#image-preview-1').attr('src', e.target.result).css('display', 'block')
            };

            reader.readAsDataURL(input.files[0]);
        }
    }

    $(document).ready(function () {
        $('#id_image').change(function () {
            readURL(this);
        });
    });
})