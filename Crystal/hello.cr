class helloWorld
	def initialize(@name : String)
	end

	def greet
		puts "Hello #{@name}!"
	end
	end

greeter = helloWorld.new("world")
greeter.salute

