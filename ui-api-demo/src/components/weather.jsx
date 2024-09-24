"use client"

import { useState, useEffect } from "react"




import { Button, Card, CardBody, CardHeader, Input, Skeleton } from "@nextui-org/react"
// import json from "./response.json"
import data from "./response.json"
import { LucideSun, LucideDroplet, LucideWind, LucideCloud } from "lucide-react"
import Destination from "./destination"
import axios from "axios"
import debounce from "../utils/tools"
// This is a placeholder. Replace with your actual API key and endpoint


export default function WeatherForecast() {
  const [city, setCity] = useState("")
  const [params, setparams] = useState({
    q: "",
    page: 1,
    per_page: 1,
    show_all: false
  })
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState("")
  const [forecast, setForecast] = useState([])

  const fetchWeather = async () => {
    if (params.q === "") {
      setError("Please enter a city name")
      return
    }
    if(/\D/.test(params.per_page)) {
      setError("Please enter a valid number for cities per page")
      return
    }
    setError("")
    setLoading(true)
    let url = `${import.meta.env.VITE_API_URI}/api/weather?q=${params.q}&page=${params.page}&per_page=${params.per_page}&show_all=${params.show_all}`
    try {
      const response = await axios.get(url)
      setLoading(false)
      setForecast(response.data.data)
    } catch (error) {
      setError(error.message)
      setLoading(false)
    }

    

    setTimeout(() => {
      setLoading(false)
    }, 4000)
  }
  
  useEffect(() => {
    debounce( () => setparams({...params,q: city}), 500)
  }, [city])

  useEffect(() => {
    fetchWeather()
  }, [params])

  
  


  return (
    <div className="container mx-auto p-4">
      <h1 className="text-3xl font-bold mb-6 text-center">5-Day Weather Forecast</h1>
      <div className="flex flex-col gap-2 mb-6">
        <Input
          type="text"
          placeholder="Enter city name"
          value={city}
          onChange={(e) => setCity(e.target.value)}
          className="flex-grow"
        />
        <Input
        label="Cities per page (recomended: 3)"
          type="number"
          value={params.per_page}
          onChange={(e) => {
            setparams({ ...params, per_page: e.target.value })
          }}
          className="flex-grow"
        />
     
        
        
      </div>
      {error && (
        <div className="bg-primary-100 border-l-4 border-primary-500 text-primary-700 p-4 mb-4" role="alert">
    
          <p>{error}</p>
        </div>
      )}
      <Skeleton  isLoaded={!loading} className="w-full min-h-[300px]">
      <div className="flex flex-col gap-2">
        {forecast?.map((destination, index) => (
          <Destination key={index} destination={destination} />
        ))}
      </div>
      </Skeleton>
    </div>
  )
}