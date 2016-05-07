'use strict';

angular.module('MirrorStore.index', ['ngRoute'])

    .config(['$routeProvider', function ($routeProvider) {
        $routeProvider.when('/', {
            templateUrl: 'index/index.html'
        });
    }])

    .controller('SliderCtrl', function ($scope, $http) {
        $http.get('/api/slider/1/').success(function (data) {
            $scope.slides = data.slides;
        });

    })

    .controller('NewProductsCtrl', function ($scope, $http) {
        $scope.products = false;
        $http.get('/api/products/?page_size=6&is_new=True&ordering=-time_add').success(function (data) {
            $scope.products = data.results;

        });

    })

    .controller('SaleProductsCtrl', function ($scope, $http) {
        $scope.products = false;
        $http.get('/api/products/?page_size=6&is_sale=True&ordering=-time_add').success(function (data) {
            $scope.products = data.results;
        });
    })

    .directive('rsSlider', [function () {
        return {
            'link': function (scope, elem, attrs) {

                if(scope.$last) {
                    $(elem.parent()).responsiveSlides({
                        auto: true,
                        pager: true,
                        nav: true,
                        speed: 1000,
                        namespace: "centered-btns"
                    });
                    
                }
            }
        };
    }]);


