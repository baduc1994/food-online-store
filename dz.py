davur_folder_name = "davur"
frontend_folder_name = "frontend"

dz_array = {
    "davur": {
        "davur_views": {
            "public": {
                "favicon": f"{davur_folder_name}/images/favicon.png",
                "title": "Davur - Restaurant Django Admin Dashboard + FrontEnd",
                "social_image_url": "https://davur.dexignzone.com/django/social-image.png"
            },
            "global": {
                "css": [
                    f"{davur_folder_name}/vendor/bootstrap-select/dist/css/bootstrap-select.min.css",
                    f"{davur_folder_name}/css/style.css"
                ],
                "js": {
                    "top": [
                        f"{davur_folder_name}/vendor/global/global.min.js",
                        f"{davur_folder_name}/vendor/bootstrap-select/dist/js/bootstrap-select.min.js"
                    ],
                    "bottom": [
                        f"{davur_folder_name}/js/custom.js",
                        f"{davur_folder_name}/js/deznav-init.js",
                    ]
                },

            },
            "pagelevel": {
                "css": {
                    "index": [
                        f"{davur_folder_name}/vendor/jqvmap/css/jqvmap.min.css",
                        f"{davur_folder_name}/vendor/chartist/css/chartist.min.css"
                    ],
                    "page_analytics": [
                        f"{davur_folder_name}/vendor/jqvmap/css/jqvmap.min.css",
                        f"{davur_folder_name}/vendor/chartist/css/chartist.min.css"
                    ],
                    "page_review": [
                        f"{davur_folder_name}/vendor/jqvmap/css/jqvmap.min.css",
                        f"{davur_folder_name}/vendor/chartist/css/chartist.min.css",
                        f"{davur_folder_name}/vendor/owl-carousel/owl.carousel.css"
                    ],
                    "page_general_customers": [
                        f"{davur_folder_name}/vendor/datatables/css/jquery.dataTables.min.css"
                    ],
                    "users": [
                        f"{davur_folder_name}/vendor/sweetalert2/dist/sweetalert2.min.css",
                    ],
                    "add_user": [
                        f"{davur_folder_name}/vendor/bootstrap-daterangepicker/daterangepicker.css",
                        f"{davur_folder_name}/vendor/select2/css/select2.min.css",
                    ],
                    "edit_user": [
                        f"{davur_folder_name}/vendor/bootstrap-daterangepicker/daterangepicker.css",
                        f"{davur_folder_name}/vendor/select2/css/select2.min.css",
                    ],
                    "assign_permissions_to_user": [

                        f"{davur_folder_name}/vendor/bootstrap-duallistbox/ajax/libs/prettify/r298/prettify.min.css",
                        f"{davur_folder_name}/vendor/bootstrap-duallistbox/src/bootstrap-duallistbox.css",
                        f"{davur_folder_name}/vendor/bootstrap-duallistbox/dist/bootstrap-duallistbox.css",
                    ],

                    "group_add": [
                        f"{davur_folder_name}/vendor/bootstrap-duallistbox/ajax/libs/prettify/r298/prettify.min.css",
                        f"{davur_folder_name}/vendor/bootstrap-duallistbox/src/bootstrap-duallistbox.css",
                        f"{davur_folder_name}/vendor/bootstrap-duallistbox/dist/bootstrap-duallistbox.css",
                    ],

                    "group_edit": [
                        f"{davur_folder_name}/vendor/bootstrap-duallistbox/ajax/libs/prettify/r298/prettify.min.css",
                        f"{davur_folder_name}/vendor/bootstrap-duallistbox/src/bootstrap-duallistbox.css",
                        f"{davur_folder_name}/vendor/bootstrap-duallistbox/dist/bootstrap-duallistbox.css",
                    ],

                    "app_profile": [
                        f"{davur_folder_name}/vendor/lightgallery/css/lightgallery.min.css",
                        f"{davur_folder_name}/vendor/magnific-popup/magnific-popup.css"
                    ],
                    "post_details": [
                        f"{davur_folder_name}/vendor/lightgallery/css/lightgallery.min.css",
                        f"{davur_folder_name}/vendor/magnific-popup/magnific-popup.css"
                    ],
                    "ecom_product_list": [],
                    "ecom_product_order": [],
                    "page_forgot_password": [],
                },
                ##********************************************************

                # Javascript

                # **********************************************************
                "js": {
                    "index": [
                        f"{davur_folder_name}/vendor/chart.js/Chart.bundle.min.js",
                        f"{davur_folder_name}/js/deznav-init.js",
                        f"{davur_folder_name}/vendor/waypoints/jquery.waypoints.min.js",
                        f"{davur_folder_name}/vendor/jquery.counterup/jquery.counterup.min.js",
                        f"{davur_folder_name}/vendor/apexchart/apexchart.js",
                        f"{davur_folder_name}/vendor/peity/jquery.peity.min.js",
                        f"{davur_folder_name}/js/dashboard/dashboard-1.js"
                    ],
                    "page_analytics": [
                        f"{davur_folder_name}/vendor/waypoints/jquery.waypoints.min.js",
                        f"{davur_folder_name}/vendor/jquery.counterup/jquery.counterup.min.js",
                        f"{davur_folder_name}/vendor/peity/jquery.peity.min.js",
                        f"{davur_folder_name}/vendor/apexchart/apexchart.js",
                        f"{davur_folder_name}/js/dashboard/analytics.js"
                    ],
                    "page_review": [
                        f"{davur_folder_name}/vendor/owl-carousel/owl.carousel.js"
                    ],
                    "page_general_customers": [
                        f"{davur_folder_name}/vendor/datatables/js/jquery.dataTables.min.js"
                    ],
                    "users": [
                        f"{davur_folder_name}/vendor/sweetalert2/dist/sweetalert2.min.js",

                    ],
                    "add_user": [
                        f"{davur_folder_name}/vendor/moment/moment.min.js",
                        f"{davur_folder_name}/vendor/bootstrap-daterangepicker/daterangepicker.js",
                        f"{davur_folder_name}/vendor/select2/js/select2.full.min.js",
                        f"{davur_folder_name}/js/plugins-init/select2-init.js"
                    ],
                    "edit_user": [
                        f"{davur_folder_name}/vendor/moment/moment.min.js",
                        f"{davur_folder_name}/vendor/bootstrap-daterangepicker/daterangepicker.js",
                        f"{davur_folder_name}/vendor/select2/js/select2.full.min.js",
                        f"{davur_folder_name}/js/plugins-init/select2-init.js"
                    ],
                    "assign_permissions_to_user": [
                        f"{davur_folder_name}/vendor/bootstrap-duallistbox/ajax/libs/popper.js/1.12.9/umd/popper.min.js",
                        f"{davur_folder_name}/vendor/bootstrap-duallistbox/ajax/libs/prettify/r298/run_prettify.js",
                        f"{davur_folder_name}/vendor/bootstrap-duallistbox/dist/jquery.bootstrap-duallistbox.js",
                    ],
                    "group_add": [
                        f"{davur_folder_name}/vendor/bootstrap-duallistbox/ajax/libs/popper.js/1.12.9/umd/popper.min.js",
                        f"{davur_folder_name}/vendor/bootstrap-duallistbox/ajax/libs/prettify/r298/run_prettify.js",
                        f"{davur_folder_name}/vendor/bootstrap-duallistbox/dist/jquery.bootstrap-duallistbox.js",
                    ],

                    "group_edit": [
                        f"{davur_folder_name}/vendor/bootstrap-duallistbox/ajax/libs/popper.js/1.12.9/umd/popper.min.js",
                        f"{davur_folder_name}/vendor/bootstrap-duallistbox/ajax/libs/prettify/r298/run_prettify.js",
                        f"{davur_folder_name}/vendor/bootstrap-duallistbox/dist/jquery.bootstrap-duallistbox.js",
                    ],

                    "app_profile": [
                        f"{davur_folder_name}/vendor/lightgallery/js/lightgallery-all.min.js",
                        f"{davur_folder_name}/vendor/magnific-popup/jquery.magnific-popup.js"

                    ],
                    "post_details": [
                        f"{davur_folder_name}/vendor/lightgallery/js/lightgallery-all.min.js",
                        f"{davur_folder_name}/vendor/magnific-popup/jquery.magnific-popup.js"

                    ],
                    "ecom_product_list": [
                        f"{davur_folder_name}/vendor/highlightjs/highlight.pack.min.js",
                        f"{davur_folder_name}/vendor/star-rating/jquery.star-rating-svg.js",
                    ],
                    "ecom_product_order": [
                        f"{davur_folder_name}/vendor/chart.js/Chart.bundle.min.js",
                        f"{davur_folder_name}/vendor/apexchart/apexchart.js",
                        f"{davur_folder_name}/vendor/highlightjs/highlight.pack.min.js",
                    ],
                    "page_forgot_password": [],

                }

            }

        }  # davur end
    },
    "frontend": {
        "frontend_views": {
            "public": {
                "favicon": f"{frontend_folder_name}/images/favicon.png",
                "title": "Davur - Restaurant Django Admin Dashboard + FrontEnd",
                "social_image_url": "https://davur.dexignzone.com/django/social-image.png"
            },
            "global": {
                "css": [
                    f"{frontend_folder_name}/vendor/bootstrap-select/dist/css/bootstrap-select.min.css",
                    f"{frontend_folder_name}/css/style.css"
                ],
                "js": {
                    "top": [
                        f"{frontend_folder_name}/vendor/global/global.min.js",
                        f"{frontend_folder_name}/vendor/bootstrap-select/dist/js/bootstrap-select.min.js"
                    ],
                    "bottom": [
                        f"{frontend_folder_name}/js/custom.js",
                        f"{frontend_folder_name}/js/deznav-init.js",
                    ]
                },

            },
            "pagelevel": {
                "css": {
                    "front_home": [
                        f"{frontend_folder_name}/vendor/owl-carousel/owl.carousel.css",
                        f"{frontend_folder_name}/vendor/bootstrap-touchspin/css/jquery.bootstrap-touchspin.min.css",
                        f"{frontend_folder_name}/vendor/swiper/css/swiper-bundle.css",
                    ],
                    "front_authentication": [],
                    "front_upload_item": [
                        f"{frontend_folder_name}/vendor/datatables/css/jquery.dataTables.min.css",
                    ],
                    "front_login": [],
                    "page_register": [],
                },
                "js": {
                    "front_home": [
                        f"{frontend_folder_name}/vendor/waypoints/jquery.waypoints.min.js",
                        f"{frontend_folder_name}/vendor/jquery.counterup/jquery.counterup.min.js",
                        f"{frontend_folder_name}/vendor/owl-carousel/owl.carousel.js",
                        f"{frontend_folder_name}/vendor/bootstrap-touchspin/js/jquery.bootstrap-touchspin.min.js",
                    ],
                    "front_authentication": [],
                    "front_upload_item": [
                        f"{frontend_folder_name}/vendor/waypoints/jquery.waypoints.min.js",
                        f"{frontend_folder_name}/vendor/jquery.counterup/jquery.counterup.min.js",
                        f"{frontend_folder_name}/vendor/datatables/js/jquery.dataTables.min.js",
                    ],
                    "front_login": [],
                    "page_register": [],
                }
            }
        }
    }
}
