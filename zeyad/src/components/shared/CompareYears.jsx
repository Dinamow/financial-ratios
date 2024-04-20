import React from "react";
import { Button } from "../ui/button";
import { Link } from "react-router-dom";
import {
  Select,
  SelectContent,
  SelectGroup,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from "../ui/select";
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuLabel,
  DropdownMenuSeparator,
  DropdownMenuTrigger,
} from "../ui/dropdown-menu";
import { ArrowDown } from "lucide-react";
function CompareYears() {
  const years = [2022, 2021, 2020, 2019];
  const [year, setYear] = React.useState();
  const [year2, setYear2] = React.useState();
  return (
    <DropdownMenu>
      <DropdownMenuTrigger asChild>
        <h2 className="hidden md:flex gap-2 items-center border rounded-full p-2 px-10 bg-slate-200 cursor-pointer">
          Compare between 2 years
          <ArrowDown className="h-5 w-5 animate-bounce" />
        </h2>
      </DropdownMenuTrigger>
      <DropdownMenuContent className="w-56">
        <DropdownMenuLabel>Choose year</DropdownMenuLabel>
        <DropdownMenuSeparator />
        <div className="flex flex-col items-center justify-center gap-3">
          <Select value={year} onValueChange={setYear}>
            <SelectTrigger className="w-full">
              <SelectValue placeholder="Select year" />
            </SelectTrigger>
            <SelectContent>
              <SelectGroup>
                {years.map((year) => (
                  <SelectItem key={year} value={year}>
                    {year}
                  </SelectItem>
                ))}
              </SelectGroup>
            </SelectContent>
          </Select>
          <Select value={year2} onValueChange={setYear2}>
            <SelectTrigger className="w-full">
              <SelectValue placeholder="Select year" />
            </SelectTrigger>
            <SelectContent>
              <SelectGroup>
                {years.map((year) => (
                  <SelectItem key={year} value={year}>
                    {year}
                  </SelectItem>
                ))}
              </SelectGroup>
            </SelectContent>
          </Select>
          <Link className="w-full" to={`/ratio/${year}`}>
            <Button className="w-full mt-4">Go</Button>
          </Link>
        </div>
      </DropdownMenuContent>
    </DropdownMenu>
  );
}

export default CompareYears;
