<script>

</script>

<svelte:head>
	<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
</svelte:head>


<div class="container">
    <div class="row height d-flex justify-content-center align-items-center">
        <div class="col-md-8">
            <div class="search"> <i class="fa fa-search"></i> <input type="text" class="form-control" placeholder="Search for the video"> <button class="btn btn-primary">Search</button> </div>
        </div>
    </div>
</div>

<style>
    @import url("https://fonts.googleapis.com/css2?family=Poppins:weight@100;200;300;400;500;600;700;800&display=swap");


    .search {
        position: relative;
        box-shadow: 0 0 40px rgba(51, 51, 51, .1)
    }

    .search input {
        height: 60px;
        text-indent: 25px;
        border: 2px solid #d6d4d4
    }

    .search input:focus {
        box-shadow: none;
        border: 2px solid blue
    }

    .search .fa-search {
        position: absolute;
        top: 20px;
        left: 16px
    }

    .search button {
        @apply bg-blue-600 absolute;
        top: 5px;
        right: 5px;
        height: 50px;
        width: 110px;
        
    }
</style>