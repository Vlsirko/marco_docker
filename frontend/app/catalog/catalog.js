'use strict';

angular.module('MirrorStore.catalog', ['ngRoute'])

    .config(['$routeProvider', function($routeProvider) {
        $routeProvider.when('/:category', {
            templateUrl: 'catalog/catalog.html',
            controller: 'catalogCtrl'
        });
    }])

    .controller('catalogCtrl', function($scope, $routeParams, Product) {
        var category = $routeParams.category;
        var page = $routeParams.page;
        var pageString = page ? '&page=' . page : '';

        Product.getByCategorySlug({category__url: category}, function (data) {
            $scope.products = data.results;
        });
    });


