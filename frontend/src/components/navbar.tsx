import {ThemeModeToggle} from "@/components/theme-toggle";

const Navbar = () => (
    <nav className={`w-full flex justify-between items-center py-2 px-4 md:px-10`}>
        <div>
            <h4 className={`text-4xl text-rose-600 font-semibold`}>CodeSnap</h4>
        </div>
        <div>
            <ThemeModeToggle/>
        </div>
    </nav>
);

export default Navbar;