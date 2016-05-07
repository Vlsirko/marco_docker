'use strict';

angular.module('MirrorStore.catalog', ['ngRoute'])

    .config(['$routeProvider', function($routeProvider) {
        $routeProvider.when('/:category', {
            templateUrl: 'catalog/catalog.html',
            controller: 'catalogCtrl'
        });
    }])

    .controller('catalogCtrl', function($scope, $http, $routeParams) {
        var category = $routeParams.category;
        var page = $routeParams.page;
        var pageString = page ? '&page=' . page : '';
        $http.get('/api/products/?category__url=' + category + pageString).success(function(data) {
            $scope.products = data.results;
            console.log( data.results)
        });
    });


