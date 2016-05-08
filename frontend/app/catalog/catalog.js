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

        $scope.orderingParams = [
            {'order': '+price', 'title': 'По возрастанию цены'},
            {'order': '-price', 'title': 'По убыванию цены'},
            {'order': '+title', 'title': 'По названию'},
            {'order': '+is_preorder', 'title': 'По наличию'}
        ];

        $scope.defaultOrdering = $scope.orderingParams[3];
        if ($routeParams.ordering) {
            for (var index in $scope.orderingParams) {
                if ($scope.orderingParams[index].order === $routeParams.ordering) {
                    break;
                }
            }
            $scope.defaultOrdering = $scope.orderingParams[index];
        }

        $scope.pageSizes = [12, 24, 36];
        $scope.pageSize = $routeParams.page_size ? $routeParams.page_size : $scope.pageSizes[0];

        Product.getByCategorySlug({
            category__url: category,
            ordering: $scope.defaultOrdering['order'],
            page_size: $scope.pageSize,
            page: page
        }, function (data) {
            $scope.products = data.results;
            $scope.currPage = data.current;
            $scope.pages = Array.from(Array(data.num_pages).keys());
        });

        $scope.changeOrdering = function () {
            $location.search(
                angular.extend(
                    $location.search(),
                    {ordering: $scope.defaultOrdering.order}
                )
            );
        };

        $scope.changePageSize = function () {
            $location.search(
                angular.extend(
                    $location.search(),
                    {page_size: $scope.pageSize}
                )
            );
        };

        $scope.changePage = function (page) {
            $location.search(
                angular.extend(
                    $location.search(),
                    {page: page}
                )
            );
            $window.scrollTo(0, 0);
        }
    })
    .directive('scrollOnClick', function () {
        return {
            restrict: 'A',
            link: function (scope, $elm) {
                $elm.on('click', function () {
                    $("body").animate({scrollTop: 0}, "slow");
                });
            }
        }
    });
;


