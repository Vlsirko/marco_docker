'use strict';

angular.module('MirrorStore.catalog', ['ngRoute'])

    .config(['$routeProvider', function ($routeProvider) {
        $routeProvider.when('/c/:category', {
            templateUrl: 'catalog/catalog.html',
            controller: 'catalogCtrl'
        });
    }])

    .controller('catalogCtrl', function ($rootScope ,$scope, $routeParams, $location, $window, Product, Category) {
       
        var page = $routeParams.page ? $routeParams.page : 1;
        $scope.ordering = $routeParams.ordering ? $routeParams.ordering : '+is_preorder';
        $scope.pageSize = $routeParams.page_size ? $routeParams.page_size : 12;

        Category.get({slug: $routeParams.category}, function(data){

            $rootScope.title = data.seo_block.title;
            $rootScope.description = data.seo_block.description;
            $rootScope.meta = data.seo_block.meta;
            $rootScope.keywords = data.seo_block.keywords;

            Product.getByCategorySlug({
                category: data.id,
                ordering: $scope.ordering,
                page_size: $scope.pageSize,
                page: page
            }, function (data) {
                $scope.products = data.results;
                $scope.currPage = data.current;
                $scope.pagesCount = data.num_pages;
            });
        });


    });


