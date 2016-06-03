'use strict';

angular.module('MirrorStore.card', ['ngRoute'])

    .config(['$routeProvider', function($routeProvider) {
        $routeProvider.when('/:parent_category/:category/:product', {
            templateUrl: 'card/card.html',
            controller: 'cardCtrl'
        });
    }])

    .controller('cardCtrl', function($rootScope, $scope, $routeParams, Product) {
        Product.get({slug: $routeParams.product}, function (data) {

            if(data.seo_block){
                $rootScope.title = data.seo_block.title;
                $rootScope.description = data.seo_block.description;
                $rootScope.meta = data.seo_block.meta;
                $rootScope.keywords = data.seo_block.keywords;
            }

            $scope.product = data;
        });
    });