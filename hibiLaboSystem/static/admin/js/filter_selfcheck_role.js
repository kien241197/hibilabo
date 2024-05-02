var script = document.createElement('script');
script.src = 'https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js';
script.onload = function () {
    $(document).ready(function () {

        function callApi(){
            let str = "";
            const valueRole = $("#id_role").val()
            const valueCompany = $("#id_company").val()

            if (valueRole && valueCompany) {
                const url = `/ajax/filter-selfcheck-role/${valueRole}/${valueCompany}`
                $.ajax({
                    url,
                    success: function (res) {
                        const data = res;
                        if (data?.status === "200") {
                            data?.data?.map((item, index) => {
                                str += `<div>
                                <label for="id_selfcheck_roles_${index}">
                                    <input 
                                        type="checkbox" 
                                        value=${item.id} ${data?.selfcheckRoleCompany && data?.selfcheckRoleCompany[index]?.id === item?.id ? `checked` : ''} 
                                        name="selfcheck_roles" id="id_selfcheck_roles_${item.id}">
                                    ${item.selfcheck_role_name}
                                </label>
                                </div>`
                            })

                            $("#id_selfcheck_roles").html(str)
                        }
                    }

                })
            }
            else {
                $("#id_selfcheck_roles").html(str)
            }
        }

        $("#id_role").click(function () {
            callApi()
        })

        $("#id_company").click(function () {
            callApi()
        })

        function defaultData() {
            callApi()
        }

        defaultData()
    });
};
document.head.appendChild(script);