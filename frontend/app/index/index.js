'use strict';

angular.module('MirrorStore.index', ['ngRoute'])

    .config(['$routeProvider', function ($routeProvider) {
        $routeProvider.when('/', {
            templateUrl: 'index/index.html',
            controller: 'indexCtrl'
        });
    }])

    .controller('indexCtrl', function ($scope, Slider, Product) {

        Slider.get({id: 1}, function(slider){
            $scope.slides = slider.gallery;
        });

        Product.getNew(function(products){
            $scope.products = products.results;
        });

        Product.getSale(function(products){
            $scope.productsSale = products.results;
        });
    });



