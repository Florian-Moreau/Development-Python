Alpha = 1
myfile = open('myfile.txt', 'w')
for x in range(1, 2):
	myfile.write("""
	<div class="work-item hover-trigger hover-2">
              <div class="work-container">
                <div class="work-img">
                  <a href="img/portfolio/mixed_width/""" + str(Alpha) + """.jpg" class="lightbox-img" >
                    <img src="img/portfolio/mixed_width/""" + str(Alpha) + """.jpg" alt="">
                    <div class="hover-overlay" data-overlay="5">                    
                    </div>
                  </a>              
                </div>                  
              </div> 
            </div> <!-- end work-item -->
			""")
	Alpha += 1
myfile.close()
