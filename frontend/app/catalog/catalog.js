'use strict';

angular.module('MirrorStore.catalog', ['ngRoute'])

    .config(['$routeProvider', function ($routeProvider) {
        $routeProvider.when('/:category', {
            templateUrl: 'catalog/catalog.html',
            controller: 'catalogCtrl'
        });
    }])

    .controller('catalogCtrl', function ($scope, $routeParams, $location, $window, Product) {
        var category = $routeParams.category;
        var page = $routeParams.page ? $routeParams.page : 1;
        $scope.ordering = $routeParams.ordering ? $routeParams.ordering : '+is_preorder';
        $scope.pageSize = $routeParams.page_size ? $routeParams.page_size : 12;

        Product.getByCategorySlug({
            category__url: category,
            ordering: $scope.ordering,
            page_size: $scope.pageSize,
            page: page
        }, function (data) {
            $scope.products = data.results;
            $scope.currPage = data.current;
            $scope.pagesCount = data.num_pages;
        });
    });


