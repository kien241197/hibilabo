$(document).ready(function () {


    function readURL(input) {
        if (input.files && input.files[0]) {
            var reader = new FileReader();

            console.log("vao day")
            reader.onload = function (e) {
                $('#image-preview').attr('src', e.target.result);
                $('#image-preview-1').attr('src', e.target.result).css('display', 'block')
                $('#delete-image').css('display', 'block')

            };

            reader.readAsDataURL(input.files[0]);
        }
    }

    $('#id_image').change(function () {
        readURL(this);
    });

    $('#delete-image').click(function () {

        $('#image-preview-1').attr('src', '').css('display', 'none')
        $(this).css('display', 'none')
        $("#id_image").val("")
    })
})