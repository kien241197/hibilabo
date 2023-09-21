
const valueElements = document.querySelectorAll('.value-table');
valueElements.forEach((element) => {
    element.addEventListener('click', () => {
        // Thêm hoặc loại bỏ class CSS mới (ví dụ: "selected")
        console.log("element", element);
        element.classList.add('background-value-table');
    });
});


// document.querySelector(".wrapper-item-table-body-bottom-right-tab-2").classList.add("hidden-tab");
// document.querySelector(".tab1").classList.add("background-tab-active")
// const valueTab1 = document.querySelector(".tab1");
// valueTab1.addEventListener('click', () => {
//     // Thêm hoặc loại bỏ class CSS mới (ví dụ: "selected")
//         valueTab1.classList.add('background-tab-active');
//         document.querySelector(".tab2").classList.remove("background-tab-active")
//         document.querySelector(".wrapper-item-table-body-bottom-right-tab-1").classList.remove("hidden-tab");
//         document.querySelector(".wrapper-item-table-body-bottom-right-tab-2").classList.add("hidden-tab");
// });

// const valueTab2 = document.querySelector(".tab2");
// valueTab2.addEventListener('click', () => {
//     // Thêm hoặc loại bỏ class CSS mới (ví dụ: "selected")
//     valueTab2.classList.add('background-tab-active');
//         document.querySelector(".tab1").classList.remove("background-tab-active")
//         document.querySelector(".wrapper-item-table-body-bottom-right-tab-1").classList.add("hidden-tab");
//         document.querySelector(".wrapper-item-table-body-bottom-right-tab-2").classList.remove("hidden-tab");
// });
console.log(window.innerWidth)